Number.prototype.pad = function(size) {
        var s = String(this);
        while (s.length < (size || 2)) {s = "0" + s;}
        return s;
}
var listener;

// Audio
var kaching = new Audio('../audio/kaching.mp3');
var what = new Audio('../audio/what.mp3');
var oooh = new Audio('../audio/oooh.mp3');
var laugh = new Audio('../audio/laugh.mp3');
var laugh2 = new Audio('../audio/laugh2.mp3');
var laugh3 = new Audio('../audio/laugh3.mp3');

// DOM elements
var correctPlayer1;
var correctPlayer2;
var incorrectPlayer1;
var incorrectPlayer2;
var matchesPlayer1;
var matchesPlayer2;
var feedbackElmts;
var timer;
var deck;
var matchedCard = [];
var closeicon;
var starsList;
var nextlevel;
var gameover;
var cards;

// timer variables
timeLimitMinutes = 0;
timeLimitSeconds = 10;

function loadGame(flip_card_callback) {
  listener = new window.keypress.Listener(); 
  correctPlayer1 = document.getElementById("correctPlayer1");
  correctPlayer2 = document.getElementById("correctPlayer2");
  incorrectPlayer1 = document.getElementById("incorrectPlayer1");
  incorrectPlayer2 = document.getElementById("incorrectPlayer2");
  matchesPlayer1 = document.getElementById("matchesPlayer1");
  matchesPlayer2 = document.getElementById("matchesPlayer2");
  feedbackElmts = [document.getElementById("feedbackPlayer1"),document.getElementById("feedbackPlayer2")];
  feedbackElmts[0].style.backgroundRepeat = 'no-repeat';
  feedbackElmts[1].style.backgroundRepeat = 'no-repeat';
  feedbackElmts[0].style.backgroundPosition = 'left';
  feedbackElmts[1].style.backgroundPosition = 'right';
  timer = document.querySelector(".timer");
  timer.innerHTML = timeLimitMinutes.pad()+":"+timeLimitSeconds.pad();
  
  
   // stars list
  starsList = document.querySelectorAll(".stars li");
  
   // close icon in modal
  closeicon = document.querySelector(".close");
  
   // declare modal
  nextlevel = document.getElementById("nextlevel")
  gameover = document.getElementById("gameover")
  // cards array holds all cards
  card = document.getElementsByClassName("card");
  cards = [...card]
  
  // deck of all cards in game
  deck = document.getElementById("card-deck");
  
  // loop to add event listeners to each card
  for (var i = 0; i < cards.length; i++){
      card = cards[i];
      card.setAttribute('data-index', i);
      //card.addEventListener("click", displayCard);
      function create_flip_card_callback(i) {
          return function() { if (!cards[i].classList.contains("disabled")) { flip_card_callback(i); } };
      }
      card.addEventListener("click", create_flip_card_callback(i));
  };
  
  startGame();
}

function reset_game(data) {
    /*
    for (var scriptId in data.scripts) {
        createScriptLoader(scriptId, data.scripts[scriptId])( () => {});
    }
    var previousScriptLoader = (() => {});
    for (var i=data.scripts.length-1; i>=0; i--) {
    data.scripts.forEach( function(script_url, index) {
    for (var script_url in data.scripts) {
        createScriptLoader(script_url)( () => {});
        previousScriptLoader = createScriptLoader(script_url)( previousScriptLoader );
    }
    }
    });
    */
    //createScriptTags(data.scripts);
    update_game(data);
}
