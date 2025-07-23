// 获取页面元素
const uploadInput = document.getElementById('uploadInput');
const originalImage = document.getElementById('originalImage');
const compressedImage = document.getElementById('compressedImage');
const originalSize = document.getElementById('originalSize');
const compressedSize = document.getElementById('compressedSize');
const qualityRange = document.getElementById('qualityRange');
const qualityValue = document.getElementById('qualityValue');
const downloadBtn = document.getElementById('downloadBtn');

let originalFile = null;
let compressedBlob = null;

// 工具函数：格式化文件大小
function formatSize(size) {
    if (size < 1024) return size + ' B';
    if (size < 1024 * 1024) return (size / 1024).toFixed(1) + ' KB';
    return (size / 1024 / 1024).toFixed(2) + ' MB';
}

// 监听上传图片
uploadInput.addEventListener('change', function (e) {
    const file = e.target.files[0];
    if (!file) return;
    if (!/image\/(png|jpeg)/.test(file.type)) {
        alert('只支持 PNG 和 JPG 格式图片！');
        return;
    }
    originalFile = file;
    // 显示原图
    const reader = new FileReader();
    reader.onload = function (evt) {
        originalImage.src = evt.target.result;
        originalImage.style.display = 'block';
        originalSize.textContent = '文件大小：' + formatSize(file.size);
        // 自动压缩
        compressImage();
    };
    reader.readAsDataURL(file);
});

// 监听压缩比例滑块
qualityRange.addEventListener('input', function () {
    qualityValue.textContent = qualityRange.value + '%';
    if (originalFile) {
        compressImage();
    }
});

// 图片压缩主逻辑
function compressImage() {
    const quality = qualityRange.value / 100;
    const img = new Image();
    img.onload = function () {
        // 创建 canvas
        const canvas = document.createElement('canvas');
        canvas.width = img.width;
        canvas.height = img.height;
        const ctx = canvas.getContext('2d');
        ctx.drawImage(img, 0, 0);
        // 压缩图片
        canvas.toBlob(function (blob) {
            compressedBlob = blob;
            const url = URL.createObjectURL(blob);
            compressedImage.src = url;
            compressedImage.style.display = 'block';
            compressedSize.textContent = '文件大小：' + formatSize(blob.size);
            downloadBtn.style.display = 'inline-block';
        }, originalFile.type, quality);
    };
    img.src = originalImage.src;
}

// 下载压缩图片
downloadBtn.addEventListener('click', function () {
    if (!compressedBlob) return;
    const a = document.createElement('a');
    a.href = URL.createObjectURL(compressedBlob);
    a.download = 'compressed_' + (originalFile ? originalFile.name : 'image');
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}); 