<script>
import data from './data/wordle_en.json'

export default {
  data () {
    return {
      turn: 1,
      word: '',
      secretWord: '',
      wordIndex: 0,
      colorsStyles: ['--wordle-gray','--wordle-yellow','--wordle-green']
    }
  },
  mounted () {
    this.turn = 1
    this.wordIndex = Math.floor(Math.random() * ((data.length + 1) - 0)) + 0
    this.secretWord = data[this.wordIndex]
    document.addEventListener('keydown', this.typed)

    console.log(this.secretWord)
  },
  methods: {
    typed(e) {    
      const parent = document.querySelector('.wordle')
      const currentRow = parent.querySelector('#row-' + this.turn)
      const letters = currentRow.children
      let validationResultArray = []

      if ((e.keyCode >= 65 && e.keyCode <= 90) && this.word.length < 5) { // validate if the key pressed is a letter and the word length is less than six (6)
        this.word += String.fromCharCode(e.keyCode)
      } else if(e.keyCode == 8 && this.word.length > 0) { // validate if the pressed key is del
          this.word = this.word.slice(0, -1)
      } else if (e.keyCode == 13 && this.word.length == 5) { // validate if the pressed key is enter and the word has the correct length(5)
        if (!this.validWord(this.word)) { // validate if the word is in database
          console.log("invalid word")
          this.clearElements(letters)
          this.word = ''
        } else if (this.turn <= 5) { // it's a valid word 
          validationResultArray = this.validateWord(letters)
          Array.from(letters).map((letter, key) => {
            letter.style.setProperty('--letter-color',`var(${this.colorsStyles[validationResultArray[key]]})`)
            letter.style.setProperty('color','#fff')
          })
          this.turn += 1
          this.word = ''
        }
        return
      } else{
          e.preventDefault()
      }

      // painting letters in html elements while writing
      let idx = 0      
      this.clearElements(letters)
      for (let letter of this.word){
        letters[idx].innerHTML = letter
        idx += 1
      }
    },
    clearElements(elements){
      Array.from(elements).map(letter => letter.innerHTML = "")
    },
    validWord(word) {
      if (data.includes(this.word.toLowerCase()))
        return true
      return false
    },
    validateWord(elements) {
      let validationArray = [false, false, false, false, false]
      let resArray = [0,0,0,0,0]
      let idx = 0
      for (let letter of this.word.toLowerCase()){
        let idx2 = 0
        for(let valLetter of this.secretWord){
          if(letter === valLetter && !validationArray[idx2]){
            validationArray[idx2] = true
            if (idx == idx2)
              resArray[idx] = 2
            else
              resArray[idx] = 1
            break
          }
          idx2 += 1
        }
        idx += 1
      }
      return resArray
    }
  }
}

</script>

<template>
  <main id="main">
    <div class="wordle">
      <div class="wordle-title"><h2>WORDLE</h2></div>
      <div class="wordle-row" id="row-1">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
      <div class="wordle-row" id="row-2">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
      <div class="wordle-row" id="row-3">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
      <div class="wordle-row" id="row-4">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
      <div class="wordle-row" id="row-5">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
      <div class="wordle-row" id="row-6">
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter " style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
        <div class="wordle-letter" style="--letter-color: var(--color-transparent);"></div>
      </div>
    </div>
  </main>
</template>

<style>
@import './assets/base.css';
</style>
