// scripts.js para la vista previa del pdf

const url = "/static/pdfs/curriculum_aitor.pdf";  // Asegúrate de que la ruta sea correcta

const loadingTask = pdfjsLib.getDocument(url);
loadingTask.promise.then(pdf => {
    pdf.getPage(1).then(page => {
        const scale = 1.5;
        const viewport = page.getViewport({ scale: scale });

        const canvas = document.getElementById('pdf-canvas');
        const context = canvas.getContext('2d');
        canvas.height = viewport.height;
        canvas.width = viewport.width;

        page.render({
            canvasContext: context,
            viewport: viewport
        });
    });
});
