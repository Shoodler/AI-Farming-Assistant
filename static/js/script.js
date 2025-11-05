document.addEventListener('DOMContentLoaded', () => {
    // ==================== Smooth Scrolling ====================
    const navLinks = document.querySelectorAll('.nav-links a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });

    // ==================== DOM Element References ====================
    const recordBtn = document.getElementById('record-btn');
    const langSelect = document.getElementById('lang-select');
    const audioFileInput = document.getElementById('audio-file-input');
    const userQuestionText = document.getElementById('user-question');
    const aiResponseText = document.getElementById('ai-response');
    const responseAudio = document.getElementById('response-audio');
    const resultsArea = document.getElementById('results-area');
    const loader = document.getElementById('loader');

    // ==================== State Management ====================
    let isRecording = false;
    let mediaRecorder;
    let audioChunks = [];

    // ==================== Event Listeners ====================
    recordBtn.addEventListener('click', toggleRecording);
    audioFileInput.addEventListener('change', handleFileUpload);

    // ==================== Helper Functions ====================
    function showLoading(isLoading) {
        loader.style.display = isLoading ? 'block' : 'none';
        recordBtn.style.display = isLoading ? 'none' : 'flex';
    }

    // ==================== Recording Functions ====================
    async function toggleRecording() {
        if (isRecording) {
            mediaRecorder.stop();
            isRecording = false;
            recordBtn.classList.remove('recording');
        } else {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                startRecording(stream);
            } catch (err) {
                alert("Microphone access is required to record audio. Please allow permission.");
            }
        }
    }

    function startRecording(stream) {
        mediaRecorder = new MediaRecorder(stream, { mimeType: 'audio/webm' });
        audioChunks = [];
        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };
        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            const audioFile = new File([audioBlob], 'user_question.webm', { type: 'audio/webm' });
            processAudio(audioFile);
        };
        mediaRecorder.start();
        isRecording = true;
        recordBtn.classList.add('recording');
    }

    // ==================== File Upload Handler ====================
    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) processAudio(file);
    }

    // ==================== Main Processing Function ====================
    function processAudio(audioFile) {
        showLoading(true);
        const formData = new FormData();
        formData.append('file', audioFile, 'user_question.webm');
        formData.append('lang', langSelect.value);

        fetch('http://127.0.0.1:5000/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            showLoading(false);
            if (data.error) {
                alert("An error occurred:\n" + data.error);
                return;
            }
            const fullAudioUrl = data.audio_url.startsWith("http")
                ? data.audio_url
                : "http://127.0.0.1:5000" + data.audio_url;
            updateUI(
                data.query_text || "Unable to transcribe audio.",
                data.response_text || "No AI response received.",
                fullAudioUrl
            );
        })
        .catch(error => {
            showLoading(false);
            alert("Request failed: " + error);
        });
    }

    // ==================== UI Update Function ====================
    function updateUI(userText, aiText, audioUrl) {
        userQuestionText.textContent = userText;
        aiResponseText.textContent = aiText;
        responseAudio.src = audioUrl;
        responseAudio.load();
        responseAudio.play().catch(() => {});
        resultsArea.style.display = 'block';
        resultsArea.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
});
