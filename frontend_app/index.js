const path = require('path')
const express = require('express')
const app = express()

app.use(express.static(path.join(__dirname, 'build')))

const PORT = process.env.PORT || 3000

app.listen(PORT, () => {
  console.log(`App running on port ${PORT}!`)
})
