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
  $('#showHangul').change((ev) => toggleHidden(ev.target, 'hangul'))
  $('#showMeaning').change((ev) => toggleHidden(ev.target, 'yarxi_meaning'))

  toggleHidden($('#showHanja')[0], 'hanja')
  toggleHidden($('#showHangul')[0], 'hangul')
  toggleHidden($('#showMeaning')[0], 'yarxi_meaning')
})
