// Utility function for email validation
function isValidEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
  
  // Form submission handler
  document.getElementById("contact-form").addEventListener("submit", async function (e) {
    e.preventDefault();
  
    // Get form values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
  
    // Reset error messages
    document.getElementById("name-error").classList.add("d-none");
    document.getElementById("email-error").classList.add("d-none");
    document.getElementById("message-error").classList.add("d-none");
    document.getElementById("form-status").innerHTML = "";
  
    // Validate form inputs
    let hasError = false;
  
    if (!name) {
      document.getElementById("name-error").classList.remove("d-none");
      hasError = true;
    }
  
    if (!isValidEmail(email)) {
      document.getElementById("email-error").classList.remove("d-none");
      hasError = true;
    }
  
    if (!message) {
      document.getElementById("message-error").classList.remove("d-none");
      hasError = true;
    }
  
    if (hasError) return;
  
    // Submit form data to backend endpoint
    try {
      const response = await fetch("http://127.0.0.1:8000/submit-message/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ name, email, message }),
      });
  
      if (response.ok) {
        document.getElementById("form-status").innerHTML =
          '<div class="text-success">Message sent successfully!</div>';
        document.getElementById("contact-form").reset();
      } else {
        document.getElementById("form-status").innerHTML =
          '<div class="text-danger">Failed to send message. Please try again later.</div>';
      }
    } catch (error) {
      document.getElementById("form-status").innerHTML =
        '<div class="text-danger">An error occurred. Please try again later.</div>';
    }
  });
  