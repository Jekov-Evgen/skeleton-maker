def get_html(name):
    CONST_HTML = f"""
<html>

<head>
<title>{name}</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="stylesheet" href="css/style.css">
<script src="js/script.js"></script>
</head>
        
<body>
<h1 id="greeting">Hello</h1>
<button onclick="changeText()">Click Me</button>
</body>

</html>
        """
        
    return CONST_HTML

CONST_CSS = """
body {
    background-color: #f0f8ff;
    font-family: Arial, sans-serif;
}

h1 {
    color: #2e8b57;
    text-align: center;
    padding: 20px;
    border: 2px solid #2e8b57; 
    border-radius: 10px;
}

button {
    display: block;
    margin: 20px auto;
    padding: 10px 20px;
    background-color: #2e8b57;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #3cb371;
}
"""


CONST_JS = """
function changeText() {
    const greeting = document.getElementById('greeting');
    greeting.innerText = 'You clicked the button!';
    greeting.style.color = '#ff4500';
}
"""