







function speak(message) {
  // Check if the Web Speech API is supported by the browser
  if ('speechSynthesis' in window) {
    // Create a new instance of SpeechSynthesisUtterance
    const utterance = new SpeechSynthesisUtterance();
    // Set the text of the utterance
    utterance.text = message;
    // Play the synthesized speech
    window.speechSynthesis.speak(utterance);
  }
}




  const app = document.getElementById('app');
  const messagesContainer = document.getElementById('messages');
  const messageForm = document.getElementById('message-form');
  const messageInput = document.getElementById('message-input'); 
const networkTypeText = document.getElementById('network-type-text');

  
  
  function addMessageToHistory(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');
  if (sender === 'user') {
  messageDiv.classList.add('user-message');
  } else {
  messageDiv.classList.add('chatbot-message');
  }
  
  const iconDiv = document.createElement('div');
  iconDiv.classList.add('icon');
  iconDiv.innerHTML = '<i class="fa fa-user"></i>';
  messageDiv.appendChild(iconDiv);
  
  const textDiv = document.createElement('div');
  textDiv.classList.add('text');
  textDiv.textContent = message;
  messageDiv.appendChild(textDiv);
  
  chatHistory.appendChild(messageDiv);
  chatHistory.scrollTop = chatHistory.scrollHeight;
  
 
  }
  
  
  
  

  // Initialize empty list of chats
  let chats = [];
  
  // Fetch chats from local storage
  const fetchChats = () => {
  const storedChats = localStorage.getItem('chats');
  if (storedChats) {

  chats = JSON.parse(storedChats);
  }
  };
  
  // Save chats to local storage
  const saveChats = () => {
  localStorage.setItem('chats', JSON.stringify(chats));
  };
  
  // Render chat messages
  
  
  const renderMessages = () => {
  messagesContainer.innerHTML = '';
  chats.forEach(chat => {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message');
  if (chat.user) {
  messageDiv.classList.add('user');
  }
  messageDiv.innerHTML = `
  <p>${chat.message}</p>
  <span class="timestamp ${chat.user ? 'user' : ''}">${chat.timestamp}</span>
  `;
  messagesContainer.appendChild(messageDiv);
  });
  messagesContainer.scrollTop = messagesContainer.scrollHeight;
  };
  



  // Send message

  const sendMessage = (message, user = true) => {
  const chat = {
  message,
  user,
  timestamp: new Date().toLocaleString()
  };
  chats.push(chat);
  saveChats();
  renderMessages();
  // Speak the message if it's from the chatbot
  if (!user) {
  speak(message);
  }
  
  };
  
  
  
  
  
  
  
  // Handle form submission
  messageForm.addEventListener('submit', e => {
  e.preventDefault();
  const message = messageInput.value;
  if (!message) {
  return;
  }
  sendMessage(message);
  checkForMatchingWords(message);
  messageInput.value = '';
  });
  
  
  // Check if message is a question and send a response
  const checkForQuestion = message => {
  for (let i = 0; i < questions.length; i++) {
  const question = questions[i];
  if (message.includes(question.question)) {
  sendMessage(question.answer, false);
  return;
  }
  }
  };
  
  const checkForMatchingWords = message => {
  // Split message into individual words
  const words = message.split(' ');
  
  // Check if any words match a stored keyword
  for (let i = 0; i < words.length; i++) {
  for (let j = 0; j < questions.length; j++) {
  const question = questions[j];
  if (question.keywords.includes(words[i])) {
  sendMessage(question.answer, false);
  return;
  }
  }
  }
  
  // If no matching keyword is found, send default response
  sendMessage('I\'m sorry, I am unable to answer that question.kindly,contact our customer services:https://www.gloworld.com/ng/business) or check your internet connection', false);
  };
  
  
  
  
  
  const greetings = [
  'Hello! How may I help you today?',
  'Hi welcome to Glo Livechat.My name is Glotecom,How can I help you',
  'Good day! How can I assist you?'
  ];
  
  const sendGreeting = () => {
  // Select a random greeting from the greetings array
  const greeting = greetings[Math.floor(Math.random() * greetings.length)];
  sendMessage(greeting, false);
  };
  
  //clear chat history
  const clearHistoryButton = document.getElementById('clear-history');
  const logoutButton = document.getElementById('logout');
  
  clearHistoryButton.addEventListener('click', () => {
  // Clear chat history
  chats = [];
  saveChats();
  renderMessages();
  });
  
  logoutButton.addEventListener('click', () => {
  // Log out the user
  localStorage.removeItem('loggedIn');
  // Redirect to login page or show login form
  });
  
  
  
 
 
 // Initialize app
 const init = () => {
 fetchChats();
 renderMessages();
 sendGreeting();
 };
 
 init();
 
 
  
  // sidebar menu-icon
  const menuIcon = document.getElementById('menu-icon');
  const sidebar = document.getElementById('sidebar');
  
  menuIcon.addEventListener('click', () => {
  sidebar.classList.toggle('open');
  });
  
  //sidebar content
  
  
  function updateNetworkType() {
  // Check online/offline status
  const online = window.navigator.onLine;
  networkTypeText.textContent = online ? 'Online' : 'Offline';
  }
  
  updateNetworkType();
  window.addEventListener('online', updateNetworkType);
  window.addEventListener('offline', updateNetworkType);
  
/*  clearHistoryButton.addEventListener('click', () => {
  // Clear chat history here
  });*/
  
  logoutButton.addEventListener('click', () => {
  // Log out the user here
  });




