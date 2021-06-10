'use strict';

const makeCommentBtn = document.querySelector('.make-comment');
const commentModalContainer = document.querySelector('#comment-modal');
const bodyContainer = document.querySelector('body');

const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};

const detectModal = () => {
  bodyContainer.style.overflow = location.hash ? 'hidden' : null;
};

(() => {
  detectModal();

  if (makeCommentBtn) {
    const closeModal = commentModalContainer.querySelector('.modal__close');
    const commentForm = commentModalContainer.querySelector('.comment-form');
    const {type: actionType, id} = makeCommentBtn.dataset;
    const commentField = commentForm.querySelector('textarea[name="comment"]');
    const csrftoken = getCookie('csrftoken');

    commentForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const form = new FormData(e.target);
      const comment = form.get('comment');

      if (comment) {
        const data = {comment, id, actionType};

        fetch('/api/make-comment/', {
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
          },
          method: 'post',
        })
          .then((response) => response.json())
          .then((response) => {
            closeModal.click();
          })
          .catch(console.error);
      }
    });

    closeModal.addEventListener('click', () => {
      commentField.value = null;
    });
  }
})();

window.addEventListener('hashchange', () => {
  detectModal();
})
