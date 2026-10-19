(() => {
  const root = document.querySelector('[data-talks-pagination]');
  if (!root) return;

  const total = Number(root.dataset.pageCount);
  if (total <= 1) return;

  const list = root.querySelector('[data-talk-list]');
  const previous = root.querySelector('[data-talk-prev]');
  const next = root.querySelector('[data-talk-next]');
  const status = root.querySelector('[data-talk-status]');
  const firstPage = Array.from(list.children);
  const isChinese = root.dataset.lang === 'zh';
  let current = 1;

  function pageFromUrl() {
    const value = new URL(window.location.href).searchParams.get('page');
    const number = Number(value);
    return /^[1-9]\d*$/.test(value || '') && Number.isSafeInteger(number) && number <= total
      ? number : 1;
  }

  function showPage(number, updateHistory = false, moveFocus = false) {
    if (number < 1 || number > total) return;
    if (number !== current) {
      if (number === 1) {
        list.replaceChildren(...firstPage);
      } else {
        const template = root.querySelector(`template[data-talk-page="${number}"]`);
        if (!template) return;
        list.replaceChildren(template.content.cloneNode(true));
      }
      current = number;
    }

    previous.disabled = current === 1;
    next.disabled = current === total;
    status.textContent = isChinese ? `第 ${current} / ${total} 页` : `Page ${current} of ${total}`;

    if (updateHistory) {
      const url = new URL(window.location.href);
      if (current === 1) url.searchParams.delete('page');
      else url.searchParams.set('page', String(current));
      window.history.pushState(null, '', url);
    }
    if (moveFocus) {
      list.scrollIntoView({ block: 'start' });
      list.focus({ preventScroll: true });
    }
  }

  previous.addEventListener('click', () => showPage(current - 1, true, true));
  next.addEventListener('click', () => showPage(current + 1, true, true));
  window.addEventListener('popstate', () => showPage(pageFromUrl(), false, true));
  showPage(pageFromUrl());
})();
