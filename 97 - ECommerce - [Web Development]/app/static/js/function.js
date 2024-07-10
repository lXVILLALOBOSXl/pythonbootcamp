function scrollContainerLeft(containerId) {
    const container = document.getElementById(containerId);
    if (container) {
      container.scrollBy({
        left: -300,
        behavior: 'smooth'
      });
    } else {
      console.error(`Container with ID ${containerId} not found.`);
    }
  }
  
  function scrollContainerRight(containerId) {
    const container = document.getElementById(containerId);
    if (container) {
      container.scrollBy({
        left: 300,
        behavior: 'smooth'
      });
    } else {
      console.error(`Container with ID ${containerId} not found.`);
    }
  }