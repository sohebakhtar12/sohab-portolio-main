js_append = """

// ── Contact Form Submission ────────────────
const contactForm = document.getElementById('contactForm');
const submitBtn = document.getElementById('submitBtn');
const submitText = document.getElementById('submitText');
const toast = document.getElementById('toast');
const toastIcon = document.getElementById('toastIcon');
const toastMessage = document.getElementById('toastMessage');

function showToast(message, isSuccess = true) {
  toastMessage.textContent = message;
  toastIcon.textContent = isSuccess ? '✓' : '✗';
  toastIcon.style.color = isSuccess ? '#22c55e' : '#ef4444';
  
  toast.classList.add('show');
  
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3500);
}

contactForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(contactForm);
  const data = Object.fromEntries(formData);
  
  submitBtn.disabled = true;
  submitText.textContent = 'Sending...';
  
  try {
    const res = await fetch("https://formsubmit.co/ajax/sohebakhtar2001@gmail.com", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      body: JSON.stringify(data)
    });
    
    if (res.ok) {
      showToast('Message sent successfully!', true);
      contactForm.reset();
    } else {
      showToast('Something went wrong. Please try again.', false);
    }
  } catch (error) {
    showToast('Failed to send message. Please try again.', false);
  } finally {
    submitBtn.disabled = false;
    submitText.textContent = 'Send Message';
  }
});
"""

css_append = """

/* ── Toast Notification ──────────────────── */
.toast {
  position: fixed;
  bottom: 30px;
  right: 30px;
  background: rgba(15, 5, 5, 0.95);
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  border: 1px solid rgba(204, 0, 0, 0.2);
  padding: 16px 24px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  gap: 14px;
  color: #fff;
  font-size: 0.92rem;
  font-weight: 500;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
  z-index: 10000;
  transform: translateY(100px);
  opacity: 0;
  pointer-events: none;
  transition: all 0.5s cubic-bezier(0.22, 1, 0.36, 1);
}

.toast.show {
  transform: translateY(0);
  opacity: 1;
}

.toast-icon {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}
"""

with open("script.js", "a", encoding="utf-8") as f:
    f.write(js_append)

with open("style.css", "a", encoding="utf-8") as f:
    f.write(css_append)
