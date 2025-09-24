 document.addEventListener('DOMContentLoaded', function() {
        // Initialize syntax highlighting
        hljs.highlightAll();
        
        // Toggle code visibility
        function setupToggleButtons(selector, dataAttribute) {
            document.querySelectorAll(selector).forEach(function(button) {
                button.addEventListener('click', function() {
                    const targetId = this.getAttribute(dataAttribute);
                    const codeContainer = document.getElementById('code-' + targetId);
                    const icon = this.querySelector('i');
                    
                    // Toggle visibility
                    codeContainer.classList.toggle('show');
                    
                    // Toggle icon and button text
                    if (codeContainer.classList.contains('show')) {
                        icon.classList.remove('fa-code');
                        icon.classList.add('fa-eye-slash');
                        this.innerHTML = this.innerHTML.replace('View Code', 'Hide Code');
                        // Re-highlight the code when shown
                        hljs.highlightElement(codeContainer.querySelector('code'));
                    } else {
                        icon.classList.remove('fa-eye-slash');
                        icon.classList.add('fa-code');
                        this.innerHTML = this.innerHTML.replace('Hide Code', 'View Code');
                    }
                });
            });
        }
        
        // Set up toggle buttons for both pending and reviewed items
        setupToggleButtons('[data-review-id]', 'data-review-id');
        setupToggleButtons('[data-submission-id]', 'data-submission-id');
        
        // Copy code functionality
        document.querySelectorAll('.copy-btn').forEach(function(button) {
            button.addEventListener('click', function() {
                const targetId = this.getAttribute('data-code-id');
                const codeBlock = document.querySelector('#code-' + targetId + ' code');
                navigator.clipboard.writeText(codeBlock.textContent).then(function() {
                    const originalText = this.innerHTML;
                    this.innerHTML = '<i class="fas fa-check"></i> Copied!';
                    setTimeout(function() {
                        button.innerHTML = originalText;
                    }, 2000);
                }.bind(this));
            });
        });
    });