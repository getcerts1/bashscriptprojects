let score = JSON.parse(localStorage.getItem('score')) || 
   
   { wins: 0,
      losses:0,
      ties:0 };
    
    updateScoreElement()


      function updateScoreElement() {
        document.querySelector('.js-score')
      .innerHTML = `wins:${score.wins}, 
      losses: ${score.losses}, ties: ${score.ties}`;

      };

      function pickComputerMove() {

      const randomNumber = Math.random();
      let computerMove = ''

      if (randomNumber >= 0 && randomNumber < 1/3) {
        computerMove = 'rock'
      } else if (randomNumber >= 1/3 && randomNumber < 2/3) {
        computerMove = 'paper'
      } else if (randomNumber >= 2/3 && randomNumber < 1) {
        computerMove = 'scissors'
      }
      
      return computerMove
    }

      function playgame (playermove) {
      const computerMove  = pickComputerMove()

      let result = ''

      if (playermove === 'scissors') {
        if (computerMove === 'rock') {
        result = 'you lose'
      } else if (computerMove === 'paper') {
        result = 'you win'
      } else if (computerMove === 'scissors') {
        result = 'Tie'
      }

     } else if (playermove === 'paper') {
      if (computerMove === 'rock') {
      result = 'you win'
      } else if (computerMove === 'paper') {
        result = 'Tie'
      } else if (computerMove === 'scissors') {
        result = 'you lose'
      }

    } else if (playermove === 'rock') {
      if (computerMove === 'rock') {
        result = 'Tie'
      } else if (computerMove === 'paper') {
        result = 'you lose'
      } else if (computerMove === 'scissors') {
        result = 'you win'
      }
    }

      if (result === 'you win') {
        score.wins += 1;
      } else if (result === 'you lose') {
        score.losses += 1
      } else if (result === 'Tie') {
        score.ties += 1
      };

     localStorage.setItem('score', JSON.stringify(score) )


     updateScoreElement()
     
     document.querySelector('.js-result')
      .innerHTML = result

    document.querySelector('.js-moves')
      .innerHTML = `you 
      <img src="${playermove}-emoji.png" class="move-icon">
      <img src="${computerMove}-emoji.png" class="move-icon">
    Computer`
    
      
    }