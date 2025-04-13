// This file contains additional JavaScript functionality for the quiz application

// Function to prevent going back to previous questions
function preventBackNavigation() {
    window.history.pushState(null, null, window.location.href)
    window.onpopstate = () => {
      window.history.pushState(null, null, window.location.href)
    }
  }
  
  // Function to detect if user is trying to open dev tools
  function detectDevTools() {
    const devtools = {
      isOpen: false,
      orientation: undefined,
    }
  
    const threshold = 160
  
    // Check if dev tools are open by comparing window width
    const emitEvent = (isOpen, orientation) => {
      window.dispatchEvent(
        new CustomEvent("devtoolschange", {
          detail: {
            isOpen,
            orientation,
          },
        }),
      )
    }
  
    setInterval(() => {
      const widthThreshold = window.outerWidth - window.innerWidth > threshold
      const heightThreshold = window.outerHeight - window.innerHeight > threshold
      const orientation = widthThreshold ? "vertical" : "horizontal"
  
      if (
        !(heightThreshold && widthThreshold) &&
        ((window.Firebug && window.Firebug.chrome && window.Firebug.chrome.isInitialized) ||
          widthThreshold ||
          heightThreshold)
      ) {
        if (!devtools.isOpen || devtools.orientation !== orientation) {
          emitEvent(true, orientation)
        }
  
        devtools.isOpen = true
        devtools.orientation = orientation
      } else {
        if (devtools.isOpen) {
          emitEvent(false, undefined)
        }
  
        devtools.isOpen = false
        devtools.orientation = undefined
      }
    }, 500)
  
    // Listen for dev tools event
    window.addEventListener("devtoolschange", (e) => {
      if (e.detail.isOpen) {
        // If dev tools are opened, submit the timeout form
        document.getElementById("timeout-form").submit()
      }
    })
  }
  
  // Function to prevent copy-paste
  function preventCopyPaste() {
    document.addEventListener("copy", (e) => {
      e.preventDefault()
      return false
    })
  
    document.addEventListener("cut", (e) => {
      e.preventDefault()
      return false
    })
  
    document.addEventListener("paste", (e) => {
      e.preventDefault()
      return false
    })
  }
  
  // Function to prevent right-click
  function preventRightClick() {
    document.addEventListener("contextmenu", (e) => {
      e.preventDefault()
      return false
    })
  }
  
  // Initialize all anti-cheating measures when the page loads
  document.addEventListener("DOMContentLoaded", () => {
    preventBackNavigation()
    detectDevTools()
    preventCopyPaste()
    preventRightClick()
  
    // Add keyboard shortcuts prevention
    document.addEventListener("keydown", (e) => {
      // Prevent F12, Ctrl+Shift+I, Ctrl+Shift+J, Ctrl+U
      if (
        e.key === "F12" ||
        (e.ctrlKey && e.shiftKey && (e.key === "I" || e.key === "i" || e.key === "J" || e.key === "j")) ||
        (e.ctrlKey && (e.key === "U" || e.key === "u"))
      ) {
        e.preventDefault()
        return false
      }
    })
  })
  