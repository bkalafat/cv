function print() {
  const baseUrl = window.location.origin + "{{ site.baseurl }}";
  const printWindow = window.open(baseUrl + "/print", "_blank");
  if (printWindow) {
    printWindow.onload = function () {
      printWindow.print();
      // Close the print window after a delay
      setTimeout(() => printWindow.close(), 500);
    };
  }
}

function generatePDF() {
  // Get the print layout URL
  const printURL = new URL("print", window.location.href).href;

  // Fetch the print layout content
  fetch(printURL)
    .then((response) => response.text())
    .then((html) => {
      // Create a temporary container
      const container = document.createElement("div");
      container.innerHTML = html;

      // Get name from the DOM (as defined in data.yml)
      const nameElement = document.querySelector(".name");
      const name = nameElement ? nameElement.textContent : "Burak_Kalafat";
      // Format filename: replace spaces with underscores and append _CV.pdf
      const filename = `${name.replace(/\s+/g, "_")}_CV.pdf`;

      // Configure pdf options
      const opt = {
        margin: 10,
        filename: filename,
        image: { type: "jpeg", quality: 0.98 },
        html2canvas: {
          scale: 2,
          useCORS: true,
          letterRendering: true,
        },
        jsPDF: {
          unit: "mm",
          format: "a4",
          orientation: "portrait",
        },
      };

      // Generate PDF
      html2pdf()
        .set(opt)
        .from(container)
        .save()
        .catch((err) => console.error("Error generating PDF:", err));
    })
    .catch((err) => console.error("Error fetching print layout:", err));
}
