function updateCheckboxDisplay(groupName, displayId) {
    const checkboxes = document.querySelectorAll(`input[name="${groupName}"]`);
    const displayBox = document.getElementById(displayId);
  
    checkboxes.forEach(cb => {
      cb.addEventListener('change', () => {
        const selected = Array.from(checkboxes)
          .filter(c => c.checked)
          .map(c => c.value);
  
        displayBox.innerHTML = selected.length
          ? `<strong>Selected:</strong> ${selected.join(", ")}`
          : '';
      });
    });
  }
  // Call function for each group
  document.addEventListener("DOMContentLoaded", function () {
    updateCheckboxDisplay('languages', 'langDisplay');
    updateCheckboxDisplay('learnSkills', 'skillDisplay');
  });
  


// function for pop message when details are submitted successfully
document.addEventListener("DOMContentLoaded", function () {
    const success_popup = document.getElementById('success_popup');
    if (success_popup) {
      success_popup.style.display = 'block';
      setTimeout(() => {
        success_popup.style.display = 'none';
      }, 3000); // disappears after 3 seconds
    }
  });