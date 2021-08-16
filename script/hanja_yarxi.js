/* global $ */

$(document).ready(() => {
  const toggleHidden = (checkbox, className) => {
    if (checkbox.checked) {
      $(`.${className}`).removeClass('hidden')
    } else {
      $(`.${className}`).addClass('hidden')
    }
  }

  $('#showHanja').change((ev) => toggleHidden(ev.target, 'hanja'))
  $('#showPronun').change((ev) => toggleHidden(ev.target, 'reading'))
  $('#showBaseMeaning').change((ev) => toggleHidden(ev.target, 'base_meaning'))
  $('#showMeaning').change((ev) => toggleHidden(ev.target, 'meaning'))

  toggleHidden($('#showHanja')[0], 'hanja')
  toggleHidden($('#showPronun')[0], 'reading')
  toggleHidden($('#showBaseMeaning')[0], 'base_meaning')
  toggleHidden($('#showMeaning')[0], 'meaning')
})
