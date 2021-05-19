$(document).on('click', '[data-toggle="lightbox"]', function (event) {
    event.preventDefault();
    $(this).ekkoLightbox();
});

<!-- popover -->
$(document).ready(function () {
    $('[data-toggle="popover"]').popover();
});

