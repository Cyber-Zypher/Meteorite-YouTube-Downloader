$(document).ready(function() {
    $('#urlInput').on('input', function() {
        var url = $(this).val();
        var videoId = extractVideoId(url);
        if (videoId) {
            var thumbnailUrl = 'https://img.youtube.com/vi/' + videoId + '/maxresdefault.jpg';
            $('#thumbnailPreview').attr('src', thumbnailUrl).show();
        } else {
            $('#thumbnailPreview').attr('src', '').hide();
        }
    });
});

function extractVideoId(url) {
    var match = url.match(/[?&]v=([^?&]+)/);
    return match ? match[1] : null;
}
