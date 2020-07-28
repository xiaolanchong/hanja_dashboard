/* global $, dalmaHanjaIndex */

function onHanjaClick (self) {
  const hanja = $(self).text()
  const hanjaBoardId = 'hanja' + hanja.charCodeAt(0)
  let hanjaBoardElem = $(`#${hanjaBoardId}`)
  if (hanjaBoardElem.length) {
    hanjaBoardElem.remove()
    return
  }
  hanjaBoardElem = $(`<div id="${hanjaBoardId}">Загрузка...</div>`)
  $(self).after(hanjaBoardElem)
  const hanjaIndex = dalmaHanjaIndex[hanja]
  if (hanjaIndex === undefined) {
    const error = 'Кандзи не найден в индексах'
    hanjaBoardElem.text(error)
    return
  }
  const hanjaUrl = 'dalma/' + articleNumberToLink(hanjaIndex)
  $.get({
    url: hanjaUrl,
    dataType: 'json'
  }
  ).done((data) => {
      hanjaBoardElem.text('')
      const table = createHanjaBoard(data)
      hanjaBoardElem.append(table)
    }
  ).fail(() => {
      hanjaBoardElem.text('Кандзи не найден на сайте')
    }
  )
  // const clicked_elem = $(event.target)
}

function createHanjaBoard (jsonData) {
  const hanja = jsonData?.hanja ?? ''
  const words = jsonData?.words ?? []
  const table = $(`<table class="hanja-board">` + 
                    `<caption>Слова ${hanja}</caption>` + 
                    `<tr><th>Ханча</th><th>Слово</th><th>Значение</th></tr>` + 
                  `</table>`)
  for (const [hanja, hangul, meaning] of words) {
    const row = $(`<tr><td class="hanja">${hanja}</td><td class="hangul">${hangul}</td><td>${meaning}</td></tr>`)
    table.append(row)
  }
  return table
}


function articleNumberToLink (number) {
  const articlesPerDir = 100
  let dirNumber = Math.floor(number / articlesPerDir)
  dirNumber = (dirNumber === 0) ? 1 : dirNumber *= articlesPerDir
  // 0001/0001.json, ..., 0900/0900.json, ...
  return padByZero(dirNumber, 4) + '/' + padByZero(number, 4) + '.json'
}

function padByZero (num, size) {
  let s = num.toString()
  while (s.length < size) { s = '0' + s }
  return s
}

const init = () => {
  $('.kanji_widget').on('click', function (event, ui) {
    onHanjaClick(this)
  })
}

window.addEventListener('load', init, false)