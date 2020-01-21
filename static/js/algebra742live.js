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
    //for (var scriptId in data.scripts) {
    //    createScriptLoader(scriptId, data.scripts[scriptId])( () => {});
    //}
    data.script.forEach( function(script_url, index) {
    //for (var script_url in data.scripts) {
        createScriptLoader(script_url)( () => {});
    //}
    });
    update_game(data);
}
function update_game(data) {
    //enable();
    players = data.players;
    active_player = data.active_player;
    screen = document.getElementById("screen");
    screen.innerHTML = data.screen_html;
    players_dashboard = document.getElementById("players-dashboard");
    //players_dashboard.innerHTML = '';
    //for(var player = 0; player < players.length; player++) {
    for(var i = 0; i < players.length; i++) {
        player = players[i]
        // update the players dashboard
        player_dashboard_id = "player-"+player.session_id+"-dashboard";
        player_dashboard = document.getElementById(player_dashboard_id);
        if (typeof(player_dashboard) == 'undefined' || player_dashboard == null) {
            player_dashboard = document.getElementById("player-dashboard-template").cloneNode(true);
            player_dashboard.style.display = "block";
            player_dashboard.id = player_dashboard_id;
            player_dashboard.classList.remove("template");
            //player_dashboard.getElementsByClassName("player-identifiers")[0].getElementsByClassName("player-nick")[0].innerHTML = "Player "+player.toString();
            player_dashboard.getElementsByClassName("player-nick")[0].innerHTML = "Player "+player.user.firstname;
            stats = player_dashboard.getElementsByClassName("player-stats")[0];
            stats.getElementsByClassName("correct")[0].getElementsByTagName("span")[0].id = "player-"+player.session_id+"-stats-correct";
            //stats.getElementsByClassName("correct")[0].id = "player-"+player.toString()+"-stats-correct";
            stats.getElementsByClassName("incorrect")[0].id = "player-"+player.session_id+"-stats-incorrect";
            stats.getElementsByClassName("matches")[0].id = "player-"+player.session_id+"-stats-matches";
            player_input_div = player_dashboard.getElementsByClassName("player-input")[0];
            player_input_div.id = "player-"+player.session_id+"-input";
            player_input_div.getElementsByClassName("yes-button")[0].id = "player-"+player.session_id+"-yes-button";
            player_input_div.getElementsByClassName("no-button")[0].id = "player-"+player.session_id+"-no-button";
            player_input_div.style.display = "none";
            players_dashboard.appendChild(player_dashboard);
        }
        if (i == active_player) {
            player_dashboard.style.background = player.color;
        } else {
            player_dashboard.removeAttribute("style");
        }
        for(var j = 0; j < player.matched_cards.length; j++){
            //alert(players[player].matched_cards[i]);
            cards[player.matched_cards[j].position].classList.add("disabled");
            cards[player.matched_cards[j].position].style.background=player.color;
        }
    }
    //window.MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    /*
    flipped_card_positions = [];
    for(var i = 0; i < flipped_cards.length; i++){
        card = cards[flipped_cards[i].position]
        card.classList.add("show", "open", "no-event");
        card.innerHTML = "$"+flipped_cards[i].info+"$";
        MathJax.Hub.Queue(["Typeset",MathJax.Hub,card]);
        flipped_card_positions.push(flipped_cards[i].position);
    }
    
    
    for(var i = 0; i < cards.length; i++){
        if (!flipped_card_positions.includes(i)) {
            cards[i].classList.remove("show", "open", "no-event");
        }
    }
    */
}


function feedback(player) {
    if(player==0) {
//        document.getElementById("feedbackPlayer1").style.display = "block";
    }
    if(player==1) {
//        document.getElementById("feedbackPlayer2").style.display = "block";
    }
}

function feedbackOff() {
  document.getElementById("feedbackPlayer1").style.display = "none";
  document.getElementById("feedbackPlayer2").style.display = "none";
}


// declaring move variable
let moves = 0;

// declare variables for star icons
const stars = document.querySelectorAll(".fa-star");

// declaring variable of matchedCards
//let matchedCard = document.querySelectorAll('.match1,.match2');

/*
 // array for opened cards
var correct = [0,0];
var incorrect = [0,0];
var speed = [0,0];
var matches = [0,0];
//var outcome = [-1,-1,-1]; // boolean values representing [do the cards match?, did player1 say they match?, did player2 say they match?]
var match = -1;
var answer = [-1,-1]
var result = [-1,-1,-1];
var openedCards = [];
var active_player = 0;
var a = 75;
var b = 50;
var c = 1;
var d = 1;

*/

// @description shuffles cards
// @param {array}
// @returns shuffledarray
function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
};


// @description shuffles cards when page is refreshed / loads
//document.body.onload = startGame();


// @description function to start a new play 
function startGame(){
    /*
    // shuffle deck
    openedCards = [];
    //cards = shuffle(cards);
    hideConfirmBoxes();
    var turnPlayer1 = $("#turnPlayer1");
    var turnPlayer2 = $("#turnPlayer2");
    turnPlayer1.show();
    turnPlayer2.hide();
    // remove all exisiting classes from each card
    for (var i = 0; i < cards.length; i++){
        deck.innerHTML = "";
        [].forEach.call(cards, function(item) {
            deck.appendChild(item);
        });
        cards[i].classList.remove("show", "open", "match1", "match2", "disabled");
    }
    // reset moves
    moves = 0;
    score = [0,0];
    //counter.innerHTML = moves;
    correctPlayer1.innerHTML = 0;
    correctPlayer2.innerHTML = 0;
    incorrectPlayer1.innerHTML = 0;
    incorrectPlayer2.innerHTML = 0;
    matchesPlayer1.innerHTML = 0;
    matchesPlayer2.innerHTML = 0;
    // reset rating
    for (var i= 0; i < stars.length; i++){
        stars[i].style.color = "#FFD700";
        stars[i].style.visibility = "visible";
    }
    //reset timer
    second = timeLimitSeconds;
    minute = timeLimitMinutes; 
    hour = 0;
    var timer = document.querySelector(".timer");
    timer.innerHTML = "0 mins 0 secs";
    */
    clearInterval(interval);
}


// @description toggles open and show class to display cards
/*var displayCard = function (){
    this.classList.toggle("open");
    this.classList.toggle("show");
    this.classList.toggle("disabled");
};
*/

var get_input = function(player, input_callback) {
    disable();
    //moveCounter();
    prompt_for_input(player, "", function yes()
    {
         //var confirmBoxPlayer1 = $("#confirmBoxPlayer1");
         //confirmBoxPlayer1.hide();
         input_callback('y');
         //i = Number(active_player!=0)+1;
         //outcome[i] = 1;
         //answer[0] = 1;
         //update_state(0);
    }, function no()
    {
         //var confirmBoxPlayer1 = $("#confirmBoxPlayer1");
         //confirmBoxPlayer1.hide();
         input_callback('n');
         //i = Number(active_player!=0)+1;
         //outcome[i] = 0;
         //answer[0] = 0;
         //update_state(0);
    });
}

/*
// @description add opened cards to OpenedCards list and check if cards are match or not
function cardOpen() {
//    openedCards.push(this);
//    //alert(openedCards);
//    var len = openedCards.length;
//    if(len === 2){
//        disable();
//        moveCounter();
//        doConfirmPlayer1("", function yes()
//        {
//             var confirmBoxPlayer1 = $("#confirmBoxPlayer1");
//             confirmBoxPlayer1.hide();
//             //i = Number(active_player!=0)+1;
//             //outcome[i] = 1;
//             answer[0] = 1;
//             update_state(0);
//        }, function no()
//        {
//             var confirmBoxPlayer1 = $("#confirmBoxPlayer1");
//             confirmBoxPlayer1.hide();
//             //i = Number(active_player!=0)+1;
//             //outcome[i] = 0;
//             answer[0] = 0;
//             update_state(0);
//        });
//        doConfirmPlayer2("", function yes()
//        {
//             var confirmBoxPlayer2 = $("#confirmBoxPlayer2");
//             confirmBoxPlayer2.hide();
//             //i = Number(active_player!=1)+1;
//             //outcome[i] = 1;
//             answer[1] = 1;
//             update_state(1);
//        }, function no()
//        {
//             var confirmBoxPlayer2 = $("#confirmBoxPlayer2");
//             confirmBoxPlayer2.hide();
//             //i = Number(active_player!=1)+1;
//             //outcome[i] = 0;
//             answer[1] = 0;
//             update_state(1);
//        });
//        //if(openedCards[0].type === openedCards[1].type){
//        //    matched();
//        //} else {
//        //    unmatched();
//        //}
//    }
};

function switch_player() {
    active_player = (active_player+1)%2;
    var turnPlayer1 = $("#turnPlayer1");
    var turnPlayer2 = $("#turnPlayer2");
    if(active_player==0) {
        document.getElementById("dashboardPlayer1").classList.add("activePlayer1");
        document.getElementById("dashboardPlayer1").classList.remove("inactivePlayer");
        document.getElementById("dashboardPlayer2").classList.add("inactivePlayer");
        document.getElementById("dashboardPlayer2").classList.remove("activePlayer2");
//    var turnPlayer1 = $("#turnPlayer1");
//    var turnPlayer2 = $("#turnPlayer2");
        turnPlayer1.show();
        turnPlayer2.hide();
    } else {
        document.getElementById("dashboardPlayer1").classList.add("inactivePlayer");
        document.getElementById("dashboardPlayer1").classList.remove("activePlayer1");
        document.getElementById("dashboardPlayer2").classList.add("activePlayer2");
        document.getElementById("dashboardPlayer2").classList.remove("inactivePlayer");
        turnPlayer2.show();
        turnPlayer1.hide();
    }
}

function checkMatch() {
    if(openedCards[0].type === openedCards[1].type){
        return(1);
    } else {
        return(0);
    }
}

function update_state(player){
    if(answer[player]!=-1) { // player1 made a decision
        if(answer[player]==checkMatch()) {
            correct[player] += 1;
            feedbackElmts[player].style.backgroundImage = 'url(../img/minion-ooo-right.jpg)';
            feedback(player);
            setTimeout(feedbackOff,3500);
        } else {
            incorrect[player] += 1;
            feedbackElmts[player].style.backgroundImage = 'url(../img/minion-waaat-right.jpg)';
            feedback(player);
            rnd = Math.floor(Math.random() * 10);
            if (rnd <= 5) {
                what.play();
            } else {
                oooh.play();
            }
            setTimeout(feedbackOff,3500);
        }
    }
    if(active_player==player && answer[player]==checkMatch()) {
        match[player] += 1;
    }
    if(answer[0]>=0 && answer[1]>=0) { // Answers are in
        if(checkMatch()) { // Match made
            if(answer[active_player]==1) { // Active player made a match and the correct decision
                kaching.play();
                matched();
            } else { // Active player made a match but an incorrect decision
                rnd = Math.floor(Math.random() * 10);
                if (rnd == 8) {
                    laugh.play();
                }
                if (rnd < 8) {
                    laugh2.play();
                }
                if (rnd == 9) {
                    laugh3.play();
                }
                unmatched();
                switch_player();
            }
        } else { // Match not made
            rnd = Math.floor(Math.random() * 10);
            if (rnd == 8) {
                laugh.play();
            }
            if (rnd < 8) {
                laugh2.play();
            }
            if (rnd == 9) {
                laugh3.play();
            }
            unmatched();
            switch_player();
        }
        answer[0]=-1
        answer[1]=-1
        correctPlayer1.innerHTML = correct[0];
        correctPlayer2.innerHTML = correct[1];
        incorrectPlayer1.innerHTML = incorrect[0];
        incorrectPlayer2.innerHTML = incorrect[1];
        matchesPlayer1.innerHTML = matches[0];
        matchesPlayer2.innerHTML = matches[1];
    }
}



// @description when cards match
function matched(){
    if (active_player == 0) {
        openedCards[0].classList.add("match1", "disabled");
        openedCards[1].classList.add("match1", "disabled");
        matches[0] += 1;
    } else {
        openedCards[0].classList.add("match2", "disabled");
        openedCards[1].classList.add("match2", "disabled");
        matches[1] += 1;
    }
    openedCards[0].classList.remove("show", "open", "no-event");
    openedCards[1].classList.remove("show", "open", "no-event");
    matchedCard.push(openedCards[0]);
    matchedCard.push(openedCards[1]);
    openedCards = [];
    enable();
    if (matchedCard.length == 2){
        congratulations();
    }
}

// @description when cards match
function failed_match(){
    openedCards[0].classList.add("failed-match", "disabled");
    openedCards[1].classList.add("failed-match", "disabled");
    openedCards[0].classList.remove("show", "open", "no-event");
    openedCards[1].classList.remove("show", "open", "no-event");
    openedCards = [];
    enable();
}


// description when cards don't match
function unmatched(){
    openedCards[0].classList.add("unmatched");
    openedCards[1].classList.add("unmatched");
    disable();
    setTimeout(function(){
        openedCards[0].classList.remove("show", "open", "no-event","unmatched");
        openedCards[1].classList.remove("show", "open", "no-event","unmatched");
        enable();
        openedCards = [];
    },1100);
}

*/

// @description disable cards temporarily
function disable(){
    Array.prototype.filter.call(cards, function(card){
        card.classList.add('disabled');
    });
}


// @description enable cards and disable matched cards
function enable(){
    Array.prototype.filter.call(cards, function(card){
        card.classList.remove('disabled');
        for(var i = 0; i < matchedCard.length; i++){
            matchedCard[i].classList.add("disabled");
        }
    });
}


// @description count player's moves
function moveCounter(){
    moves++;
    //counter.innerHTML = moves;
    //start timer on first click
    if(moves == 1){
        second = timeLimitSeconds;
        minute = timeLimitMinutes; 
        hour = 0;
        startCountdownTimer();
    }
    // setting rates based on moves
    /*
    if (moves > 8 && moves < 12){
        for( i= 0; i < 3; i++){
            if(i > 1){
                stars[i].style.visibility = "collapse";
            }
        }
    }
    else if (moves > 13){
        for( i= 0; i < 3; i++){
            if(i > 0){
                stars[i].style.visibility = "collapse";
            }
        }
    }
    */
}


// @description game timer
var interval;
function startTimer(){
    interval = setInterval(function(){
        timer.innerHTML = minute.pad()+":"+second.pad();
        second++;
        if(second == 60){
            minute++;
            second=0;
        }
        if(minute == 60){
            hour++;
            minute = 0;
        }
    },1000);
}
function startCountdownTimer(){
    interval = setInterval(function(){
        timer.innerHTML = minute.pad()+":"+second.pad();
        if(second != 00){
            second--;
        } else {
            if(minute != 00){
                second=60;
                minute--;
            } else {
                gameover.style.backgroundImage = 'url(../img/gameover.jpg)';
                gameover.style.display = "block";
            }
        }
    },1000);
}


// @description congratulations when all cards match, show modal and moves, time and rating
function congratulations(){
    clearInterval(interval);
    finalTime = timer.innerHTML;

    // show congratulations modal
    nextlevel.classList.add("show");
    nextlevel.style.display = "block";

    // declare star rating variable
    //var starRating = document.querySelector(".stars").innerHTML;

    //showing move, rating, time on modal
    //document.getElementById("finalMove").innerHTML = moves;
    //document.getElementById("starRating").innerHTML = starRating;
    //document.getElementById("totalTime").innerHTML = finalTime;

    //closeicon on modal
}


// @description close icon on modal
function closeGameover(){
    closeicon.addEventListener("click", function(e){
        gameover.classList.remove("show");
        startGame();
    });
}


// @desciption for user to play Again 
function playAgain(){
    //gameover.classList.remove("show");
    gameover.style.display = "none";
    startGame();
}



function prompt_for_input(player, msg, yesFn, noFn) {
    var player_input_div = document.getElementById("player-"+player.session_id+"-input");
    var yes_button = document.getElementById("player-"+player.session_id+"-yes-button");
    var no_button = document.getElementById("player-"+player.session_id+"-no-button");
    yes_button.addEventListener("click", function() {
        //player_input_div.classList.remove("show");
        yesFn();
        player_input_div.style.display = "none";
    });
    no_button.addEventListener("click",function() {
        //player_input_div.classList.remove("show");
        noFn();
        player_input_div.style.display = "none";
    });
    player_input_div.style.display = "block";
}

