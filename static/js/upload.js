// CropCare - Image Upload & Client Validation Script

document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.getElementById('leafImageInput');
    const dropZone = document.getElementById('dropZone');
    const previewContainer = document.getElementById('previewContainer');
    const previewImage = document.getElementById('previewImage');
    const previewName = document.getElementById('previewName');
    const previewSize = document.getElementById('previewSize');
    const btnRemove = document.getElementById('btnRemove');
    const btnSubmit = document.getElementById('btnSubmit');
    const btnSpinner = document.getElementById('btnSpinner');
    const btnText = document.getElementById('btnText');
    const uploadForm = document.getElementById('uploadForm');
    const clientAlert = document.getElementById('clientAlert');

    const MAX_SIZE_MB = 10;
    const ALLOWED_TYPES = ['image/jpeg', 'image/jpg', 'image/png', 'image/webp'];
    const ALLOWED_EXTS = ['.jpg', '.jpeg', '.png', '.webp'];

    // Helper: Show client-side error alert
    function showError(message) {
        if (!clientAlert) return;
        clientAlert.textContent = message;
        clientAlert.style.display = 'block';
    }

    // Helper: Clear client-side error alert
    function clearError() {
        if (!clientAlert) return;
        clientAlert.textContent = '';
        clientAlert.style.display = 'none';
    }

    // Helper: Format bytes to KB or MB
    function formatBytes(bytes) {
        if (bytes < 1024) return bytes + ' bytes';
        if (bytes < 1048576) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / 1048576).toFixed(2) + ' MB';
    }

    // Process selected file
    function handleFile(file) {
        clearError();

        if (!file) {
            resetUpload();
            return;
        }

        // Validate file type
        const fileName = file.name.toLowerCase();
        const hasValidExt = ALLOWED_EXTS.some(ext => fileName.endsWith(ext));
        const hasValidMime = ALLOWED_TYPES.includes(file.type);

        if (!hasValidExt && !hasValidMime) {
            showError(`Invalid file format "${file.name}". Please upload a JPG, JPEG, PNG, or WEBP image of a crop leaf.`);
            resetUpload();
            return;
        }

        // Validate file size (10 MB)
        if (file.size > MAX_SIZE_MB * 1024 * 1024) {
            showError(`File is too large (${formatBytes(file.size)}). Maximum allowed size is ${MAX_SIZE_MB} MB.`);
            resetUpload();
            return;
        }

        // Preview file using FileReader
        const reader = new FileReader();
        reader.onload = function(e) {
            previewImage.src = e.target.result;
            previewName.textContent = file.name;
            previewSize.textContent = `Size: ${formatBytes(file.size)}`;
            previewContainer.style.display = 'block';
            btnSubmit.removeAttribute('disabled');
        };
        reader.readAsDataURL(file);
    }

    // Reset upload preview & input
    function resetUpload() {
        fileInput.value = '';
        previewContainer.style.display = 'none';
        previewImage.src = '';
        previewName.textContent = '';
        previewSize.textContent = '';
        btnSubmit.setAttribute('disabled', 'true');
    }

    // Event: Native file input change
    fileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) {
            handleFile(e.target.files[0]);
        }
    });

    // Event: Click on dropzone opens file dialog
    dropZone.addEventListener('click', (e) => {
        // Prevent re-trigger if clicking browse button or internal elements
        if (e.target !== fileInput) {
            fileInput.click();
        }
    });

    // Event: Drag & Drop handlers
    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.add('dragover');
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, (e) => {
            e.preventDefault();
            e.stopPropagation();
            dropZone.classList.remove('dragover');
        });
    });

    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        if (dt.files && dt.files[0]) {
            fileInput.files = dt.files;
            handleFile(dt.files[0]);
        }
    });

    // Event: Remove button
    btnRemove.addEventListener('click', (e) => {
        e.stopPropagation();
        resetUpload();
        clearError();
    });

    // Event: Form submission with loading spinner
    uploadForm.addEventListener('submit', () => {
        btnSubmit.setAttribute('disabled', 'true');
        btnSpinner.style.display = 'inline-block';
        btnText.textContent = 'Analyzing Crop Leaf...';
    });
});
