# Python Quiz Application

![Python Quiz](https://img.shields.io/badge/Python-Quiz-blue)
![Flask](https://img.shields.io/badge/Flask-2.0.1-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A professional, interactive Python quiz application built with Flask. Test your Python knowledge with customizable quizzes featuring anti-cheating measures and detailed feedback.

 📝 Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Anti-Cheating Measures](#anti-cheating-measures)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

 ✨ Features

- Customizable Quiz Length: Choose how many questions you want to answer (5-30)
- Timed Questions: 30-second timer for each question
- Anti-Cheating Measures: Prevents tab switching, disables right-click, blocks developer tools
- Responsive Design: Works on desktop and mobile devices
- Detailed Results: Comprehensive feedback with explanations for wrong answers
- Beginner-Friendly Questions: Wide range of Python questions suitable for all skill levels
- Progress Tracking: Visual progress bar shows quiz completion status

 🎮 Demo

![Python Quiz Demo](screenshots/demo.gif)

 🚀 Installation

1. Clone the repository:
\`\`\`bash
git clone https://github.com/yourusername/python-quiz-app.git
cd python-quiz-app
\`\`\`

2. Create a virtual environment:
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

3. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

4. Run the application:
\`\`\`bash
python app.py
\`\`\`

5. Open your browser and navigate to:
\`\`\`
http://127.0.0.1:5000/
\`\`\`

 💻 Usage

1. Select the number of questions you want to answer (5-30)
2. Click "Start Quiz"
3. Answer each question within 30 seconds
4. Submit your answer or wait for the timer to expire
5. View your results and detailed explanations for wrong answers
6. Try again to improve your score!

 📁 Project Structure

\`\`\`
python-quiz-app/
├── app.py                  # Main Flask application
├── questions.py            # Quiz questions database
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── static/
│   ├── css/
│   │   └── styles.css      # Application styling
│   └── js/
│       └── app.js          # Client-side JavaScript
└── templates/
    ├── index.html          # Welcome page
    ├── quiz.html           # Quiz question page
    └── results.html        # Results page
\`\`\`

 🔒 Anti-Cheating Measures

The application implements several anti-cheating measures:

1. Timer Enforcement: Each question must be answered within 30 seconds
2. Tab/Window Detection: Quiz automatically ends if user switches tabs or windows
3. Developer Tools Detection: Detects when developer tools are opened
4. Copy/Paste Prevention: Disables copy/paste functionality
5. Right-Click Blocking: Prevents access to context menu
6. Keyboard Shortcut Blocking: Blocks common developer tool shortcuts

 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 👨‍💻 Author

John Smith

- GitHub: [@johnsmith](https://github.com/johnsmith)
- Email: john.smith@example.com
- Website: [johnsmith.dev](https://johnsmith.dev)

---

Created on: June 15, 2022
\`\`\`

