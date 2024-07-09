// // JavaScript code to add to shipment_list.html
// document.addEventListener('DOMContentLoaded', function() {
//     // Select all record lines
//     const records = document.querySelectorAll('.shipment-record');
  
//     // Add click event listener to each record
//     records.forEach(record => {
//       record.addEventListener('click', function() {
//         // Retrieve the shipment ID
//         const shipmentId = this.getAttribute('data-shipment-id');
//         // Redirect to the shipment detail page
//         window.location.href = `/shipment_detail_view/${shipmentId}/`; // Adjust the URL pattern as needed
//       });
//     });
//   });

document.addEventListener('DOMContentLoaded', function() {
  const records = document.querySelectorAll('.shipment-record');
  records.forEach(record => {
    record.addEventListener('click', function() {
      const shipmentId = this.getAttribute('data-shipment-id');
      console.log(`Shipment ID: ${shipmentId}`); // Debug log
      if (shipmentId) {
        window.location.href = `/shipment_detail_view/${shipmentId}/`;
      } else {
        console.error('Shipment ID is null or undefined.');
      }
    });
  });
});


function calculateVolume() {
  // Assuming you have fields for length, width, and height in your form
  const length = parseFloat(document.getElementById('id_shipment_length').value) || 0;
  console.log(length) // Debug log
  const width = parseFloat(document.getElementById('id_shipment_width').value) || 0;
  const height = parseFloat(document.getElementById('id_shipment_height').value) || 0;
  const volume = length * width * height;
  document.getElementById('shipment_volume_display').textContent = volume.toFixed(2); // Display volume
  document.getElementById('id_shipment_volume').value = volume.toFixed(2); // Set volume value in the form
}

document.getElementById('id_shipment_length').addEventListener('input', calculateVolume);
document.getElementById('id_shipment_width').addEventListener('input', calculateVolume);
document.getElementById('id_shipment_height').addEventListener('input', calculateVolume);

calculateVolume(); // Initial calculation