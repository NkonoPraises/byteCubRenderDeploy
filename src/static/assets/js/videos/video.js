        document.addEventListener('DOMContentLoaded', function() {
            const video = document.getElementById('videoPlayer');
            const rewindOverlayBtn = document.getElementById('rewindOverlayBtn');
            const forwardOverlayBtn = document.getElementById('forwardOverlayBtn');
            
            // Forward 10 seconds (overlay button)
            forwardOverlayBtn.addEventListener('click', function() {
                video.currentTime += 10;
            });
            
            // Rewind 10 seconds (overlay button)
            rewindOverlayBtn.addEventListener('click', function() {
                video.currentTime -= 10;
            });

        const dropdownButton = document.querySelector('.dropdown-button');
        const dropdownContent = document.querySelector('.dropdown-content');

        dropdownButton.addEventListener('click', () => {
            dropdownContent.classList.toggle('open');
            dropdownButton.classList.toggle('open');
        });

            const button = document.getElementById('interactiveButton');
            button.addEventListener('click', () => {
                alert('Hello! This is a simple interactive element triggered by JavaScript.');
            });
            
           
            // Keyboard shortcuts
            document.addEventListener('keydown', function(e) {
                // Only trigger if not focused on a button or input
                if (e.target.tagName !== 'BUTTON' && e.target.tagName !== 'INPUT') {
                    if (e.code === 'Space') {
                        e.preventDefault();
                        if (video.paused) {
                            video.play();
                        } else {
                            video.pause();
                        }
                    } else if (e.code === 'ArrowRight') {
                        video.currentTime += 10;
                    } else if (e.code === 'ArrowLeft') {
                        video.currentTime -= 10;
                    } else if (e.code === 'KeyF') {
                        if (!document.fullscreenElement) {
                            if (video.requestFullscreen) {
                                video.requestFullscreen();
                            } else if (video.webkitRequestFullscreen) {
                                video.webkitRequestFullscreen();
                            } else if (video.msRequestFullscreen) {
                                video.msRequestFullscreen();
                            }
                        } else {
                            if (document.exitFullscreen) {
                                document.exitFullscreen();
                            } else if (document.webkitExitFullscreen) {
                                document.webkitExitFullscreen();
                            } else if (document.msExitFullscreen) {
                                document.msExitFullscreen();
                            }
                        }
                    } else if (e.code === 'KeyD') {
                        descriptionContainer.classList.toggle('show');
                        if (descriptionContainer.classList.contains('show')) {
                            descriptionBtn.innerHTML = '❌';
                            descriptionBtn.setAttribute('title', 'Hide Description');
                        } else {
                            descriptionBtn.innerHTML = '📝';
                            descriptionBtn.setAttribute('title', 'Show Description');
                        }
                    }
                }
            });
        });
   