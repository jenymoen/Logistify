// JavaScript code to add to shipment_list.html
document.addEventListener('DOMContentLoaded', function() {
    // Select all record lines
    const records = document.querySelectorAll('.shipment-record');
  
    // Add click event listener to each record
    records.forEach(record => {
      record.addEventListener('click', function() {
        // Retrieve the shipment ID
        const shipmentId = this.getAttribute('data-shipment-id');
        // Redirect to the shipment detail page
        window.location.href = `/shipment_detail_view/${shipmentId}/`; // Adjust the URL pattern as needed
      });
    });
  });