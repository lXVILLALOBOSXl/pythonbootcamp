BEGIN TRANSACTION;

-- Product table without brand, category, and units fields
CREATE TABLE IF NOT EXISTS "product" (
    "id" INTEGER NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "internal_sku" VARCHAR(50) NOT NULL,
    "brand_sku" VARCHAR(50) DEFAULT 'N/A',
    "price" FLOAT NOT NULL,
    "description" TEXT DEFAULT 'N/A',
    "units_in_stock" INTEGER DEFAULT '0',
    "old_price" FLOAT,
    "is_featured" BOOLEAN DEFAULT '0',
    "date_added" DATETIME DEFAULT CURRENT_TIMESTAMP,
    "img_src" VARCHAR(255),
    UNIQUE("internal_sku"),
    PRIMARY KEY("id")
);

-- Product Image table
CREATE TABLE IF NOT EXISTS "product_image" (
    "id" INTEGER NOT NULL,
    "product_id" INTEGER NOT NULL,
    "img_src" VARCHAR(255) NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("product_id") REFERENCES "product"("id")
);

-- Category table
CREATE TABLE IF NOT EXISTS "category" (
    "id" INTEGER NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    PRIMARY KEY("id")
);

-- Tag table
CREATE TABLE IF NOT EXISTS "tag" (
    "id" INTEGER NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "category_id" INTEGER NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("category_id") REFERENCES "category"("id")
);

-- Many-to-many relationship between products and tags
CREATE TABLE IF NOT EXISTS "product_tags" (
    "product_id" INTEGER NOT NULL,
    "tag_id" INTEGER NOT NULL,
    PRIMARY KEY("product_id", "tag_id"),
    FOREIGN KEY("product_id") REFERENCES "product"("id"),
    FOREIGN KEY("tag_id") REFERENCES "tag"("id")
);

-- Other existing tables unchanged
CREATE TABLE IF NOT EXISTS "billing" (
    "id" INTEGER NOT NULL,
    "client_id" INTEGER NOT NULL,
    "rfc" VARCHAR(13) NOT NULL,
    "razon_social" VARCHAR(100) NOT NULL,
    "regimen_fiscal" VARCHAR(100) NOT NULL,
    "uso_cfdi" VARCHAR(100) NOT NULL,
    "cp" VARCHAR(5) NOT NULL,
    "is_deleted" BOOLEAN DEFAULT '0',
    PRIMARY KEY("id"),
    FOREIGN KEY("client_id") REFERENCES "client"("id")
);

CREATE TABLE IF NOT EXISTS "shipping_address" (
    "id" INTEGER NOT NULL,
    "client_id" INTEGER NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "apellidos" VARCHAR(100) NOT NULL,
    "celular" VARCHAR(10) NOT NULL,
    "empresa" VARCHAR(100),
    "calle" VARCHAR(100) NOT NULL,
    "numero" VARCHAR(10) NOT NULL,
    "num_int" VARCHAR(10),
    "referencias" VARCHAR(255),
    "colonia" VARCHAR(100) NOT NULL,
    "cp" VARCHAR(5) NOT NULL,
    "ciudad" VARCHAR(100) NOT NULL,
    "estado" VARCHAR(100) NOT NULL,
    "is_deleted" BOOLEAN DEFAULT '0',
    PRIMARY KEY("id"),
    FOREIGN KEY("client_id") REFERENCES "client"("id")
);

CREATE TABLE IF NOT EXISTS "payment_address" (
    "id" INTEGER NOT NULL,
    "client_id" INTEGER NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "apellidos" VARCHAR(100) NOT NULL,
    "calle" VARCHAR(100) NOT NULL,
    "numero" VARCHAR(10) NOT NULL,
    "num_int" VARCHAR(10),
    "referencias" VARCHAR(255),
    "colonia" VARCHAR(100) NOT NULL,
    "cp" VARCHAR(5) NOT NULL,
    "ciudad" VARCHAR(100) NOT NULL,
    "estado" VARCHAR(100) NOT NULL,
    "is_deleted" BOOLEAN DEFAULT '0',
    PRIMARY KEY("id"),
    FOREIGN KEY("client_id") REFERENCES "client"("id")
);

CREATE TABLE IF NOT EXISTS "order" (
    "id" INTEGER NOT NULL,
    "client_id" INTEGER NOT NULL,
    "date_ordered" DATETIME NOT NULL,
    "total_amount" FLOAT NOT NULL,
    "status" VARCHAR(50) NOT NULL,
    "billing_id" INTEGER,
    "shipping_address_id" INTEGER NOT NULL,
    "payment_address_id" INTEGER NOT NULL,
    "forma_de_pago" VARCHAR(100) NOT NULL,
    "metodo_de_pago" VARCHAR(100) NOT NULL,
    "tracking_number" VARCHAR(50),
    PRIMARY KEY("id"),
    FOREIGN KEY("billing_id") REFERENCES "billing"("id"),
    FOREIGN KEY("client_id") REFERENCES "client"("id"),
    FOREIGN KEY("payment_address_id") REFERENCES "payment_address"("id"),
    FOREIGN KEY("shipping_address_id") REFERENCES "shipping_address"("id")
);

CREATE TABLE IF NOT EXISTS "order_item" (
    "id" INTEGER NOT NULL,
    "order_id" INTEGER NOT NULL,
    "product_id" INTEGER NOT NULL,
    "quantity" INTEGER NOT NULL,
    "price" FLOAT NOT NULL,
    PRIMARY KEY("id"),
    FOREIGN KEY("product_id") REFERENCES "product"("id"),
    FOREIGN KEY("order_id") REFERENCES "order"("id")
);

CREATE TABLE IF NOT EXISTS "client" (
    "id" INTEGER NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "email" VARCHAR(120) NOT NULL,
    "password_hash" VARCHAR(128) NOT NULL,
    "is_verified" BOOLEAN DEFAULT '0',
    "reset_token" VARCHAR(120),
    "reset_token_expiration" DATETIME,
    "phone" VARCHAR(10) NOT NULL,
    PRIMARY KEY("id"),
    UNIQUE("email")
);

-- Insert into categories
INSERT INTO category (id, name) 
VALUES
        (1, 'Marca'),
        (2, 'Categoría'),
        (3, 'Capacidad');

-- Insert into tags
INSERT INTO tag (id, name, category_id) 
VALUES
        (1, 'LabTech', 1),
        (2, 'SpinLab', 1),
        (3, 'PipetTech', 1),
        (4, 'SafetyLab', 1),
        (5, 'MassTech', 1),
        (6, 'Centrifuga', 2),
        (7, 'Balanza', 2),
        (8, 'Cabina de Seguridad', 2),
        (9, 'Espectrómetro', 2),
        (10, 'Microscopio', 2),
        (11, '10 L', 3);

-- Insert into products
INSERT INTO product (id, name, internal_sku, brand_sku, price, description, units_in_stock, old_price, is_featured, date_added, img_src) 
VALUES
        (1, 'Microscopio Óptico', 'TC10001', 'N/A', 1499.99, 'N/A', 3, NULL, 1, '2024-07-17 19:15:18', '1.jpg'),
        (2, 'Centrífuga de Mesa', 'TC10002', 'BRD20002', 899.99, 'Centrífuga para separación de muestras en laboratorio', 14, 999.99, 0, '2024-07-17 19:15:18', NULL),
        (3, 'Espectrofotómetro UV-Vis', 'TC10003', 'N/A', 2999.99, 'N/A', 0, NULL, 1, '2024-07-17 19:15:18', NULL),
        (4, 'Balanza Analítica', 'TC10004', 'BRD20004', 499.99, 'Balanza de alta precisión para mediciones en laboratorio', 20, 599.99, 0, '2024-07-17 19:15:18', NULL),
        (5, 'Pipeta Electrónica', 'TC10005', 'N/A', 299.99, 'N/A', 20, NULL, 1, '2024-07-17 19:15:18', NULL),
        (6, 'Termociclador PCR', 'TC10006', 'N/A', 3999.99, 'N/A', 5, 4099.99, 0, '2024-07-17 19:15:18', NULL),
        (7, 'Cabina de Seguridad Biológica', 'TC10007', 'BRD20007', 5999.99, 'Protege al usuario y el medio ambiente de exposiciones peligrosas', 3, NULL, 1, '2024-07-17 19:15:18', NULL),
        (8, 'Autoclave', 'TC10008', 'N/A', 2499.99, 'N/A', 7, 2599.99, 0, '2024-07-17 19:15:18', NULL),
        (9, 'Espectrómetro de Masas', 'TC10009', 'BRD20009', 7999.99, 'Instrumento analítico para medir masas de partículas', 2, NULL, 1, '2024-07-17 19:15:18', NULL),
        (10, 'Sistema de Electroforesis', 'TC10010', 'N/A', 1299.99, 'N/A', 12, 1399.99, 0, '2024-07-17 19:15:18', NULL);

-- Insert into product_tag
INSERT INTO product_tag (product_id, tag_id) 
VALUES
        (1, 1),
        (2, 6),
        (3, 9),
        (4, 7),
        (5, 3),
        (6, 11),
        (7, 8),
        (8, 11),
        (9, 5),
        (10, 2);

-- Insert into product_image
INSERT INTO product_image (id, product_id, img_src) 
VALUES 
        (1, 1, '1.jpg'),
        (2, 1, '2.jpg');

-- Insert into client
INSERT INTO client (id,name,email,password_hash,is_verified,reset_token,reset_token_expiration,phone) VALUES (1,'Luis Adrian','ivillalobosrivera@yahoo.com','pbkdf2:sha256:600000$riEzH5gf$09c6378b5f9a5e9dad693b671ff3ca1a776e4cf42a001b043e559e99ea2b47de',1,NULL,NULL,'3313506904');

-- Insert into billing
INSERT INTO billing (id,client_id,rfc,razon_social,regimen_fiscal,uso_cfdi,cp,is_deleted) VALUES (1,1,'TCM130731SNA','TESLA CIENTIFICA MAYOREO 1','R1','U1','44900',1),(2,1,'TCM130731SNA','TESLA CIENTIFICA MAYOREO 2','R1','U1','44900',0),(3,1,'TCM130731SNA','TESLA CIENTIFICA MAYOREO 3','R1','U1','44900',0),(4,1,'TCM130731SNA','TESLA CIENTIFICA MAYOREO 4','R1','U1','44900',0),(5,1,'TCM130731SNA','TESLA CIENTIFICA MAYOREO 5','R1','U1','44900',0);

-- Insert into shipping_address 
INSERT INTO shipping_address (id,client_id,nombre,apellidos,celular,empresa,calle,numero,num_int,referencias,colonia,cp,ciudad,estado,is_deleted) VALUES (1,1,'Luis','Villalobos 1','1234567890','','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',1), (2,1,'Luis','Villalobos 2','1234567890','','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(3,1,'Luis','Villalobos 3','1234567890','','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(4,1,'Luis','Villalobos 4','1234567890','','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(5,1,'Luis','Villalobos 5','1234567890','','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0);

-- Insert into payment_address
INSERT INTO payment_address (id,client_id,nombre,apellidos,calle,numero,num_int,referencias,colonia,cp,ciudad,estado,is_deleted) VALUES (1,1,'Luis','Villalobos 1','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',1),(2,1,'Luis','Villalobos 2','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(3,1,'Luis','Villalobos 3','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(4,1,'Luis','Villalobos 4','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0),(5,1,'Luis','Villalobos 5','Tulipan Morado','128','','','Sendas Residencial','45134','Zapopan','JAL',0);

-- Insert into order
INSERT INTO order (id,client_id,date_ordered,total_amount,status,billing_id,shipping_address_id,payment_address_id,forma_de_pago,metodo_de_pago,tracking_number) VALUES (1,1,'2024-07-24 20:05:56.524241',1499.99,'Pending',1,1,1,'','','3421257825'),(2,1,'2024-07-24 20:37:37.236964',899.99,'Pending',NULL,1,1,'','',NULL),(3,1,'2024-07-24 20:38:39.783589',299.99,'Pending',NULL,1,1,'','',NULL),(4,1,'2024-07-31 16:37:10.124484',1499.99,'Pending',NULL,5,2,'','',NULL),(5,1,'2024-07-31 16:38:27.099480',1499.99,'Pending',NULL,5,2,'','',NULL),(6,1,'2024-07-31 16:39:07.898621',1499.99,'Pending',NULL,1,1,'','',NULL),(7,1,'2024-07-31 16:39:41.575438',1499.99,'Pending',NULL,5,2,'','',NULL),(8,1,'2024-08-03 16:49:30.469667',2999.98,'Pending',5,2,5,'','',NULL);

-- Insert into order_item
INSERT INTO order_item (id,order_id,product_id,quantity,price) 
VALUES 
        (1,1,1,1,1499.99),
        (2,2,2,1,899.99),
        (3,3,5,1,299.99),
        (4,4,1,1,1499.99),
        (5,5,1,1,1499.99),
        (6,6,1,1,1499.99),
        (7,7,1,1,1499.99),
        (8,8,1,2,1499.99);


COMMIT;
