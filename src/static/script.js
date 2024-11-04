function openTab(evt, tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(content => {
        content.classList.remove('active');
    });

    // Remove active class from all buttons
    const tabButtons = document.querySelectorAll('.tab-button');
    tabButtons.forEach(button => {
        button.classList.remove('active');
    });

    // Show the selected tab content and add active class to the button
    document.getElementById(tabName).classList.add('active');
    evt.currentTarget.classList.add('active');

    // Update preview and MD tab
    if (tabName === 'preview') {
        const editorContent = document.getElementById('editor').value;
        document.getElementById('preview-content').innerHTML = marked(editorContent);
    }

    if (tabName === 'md') {
        const editorContent = document.getElementById('editor').value;
        document.getElementById('md-output').value = editorContent;
    }
}

// Optional: Listen for input changes in the editor and update the preview
document.getElementById('editor').addEventListener('input', () => {
    const previewTab = document.querySelector('.tab-button.active').innerText === 'Preview';
    if (previewTab) {
        const editorContent = document.getElementById('editor').value;
        document.getElementById('preview-content').innerHTML = marked(editorContent);
    }
});
