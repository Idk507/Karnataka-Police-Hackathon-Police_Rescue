
function updateTimer() {
    future = Date.parse("Dec 19, 2023 11:30:00");
    now = new Date();
    diff = future - now;

    days = Math.floor(diff / (1000 * 60 * 60 * 24));
    hours = Math.floor(diff / (1000 * 60 * 60));
    mins = Math.floor(diff / (1000 * 60));
    secs = Math.floor(diff / 1000);

    d = days;
    h = hours - days * 24;
    m = mins - hours * 60;
    s = secs - mins * 60;

    document.getElementById("timer")
        .innerHTML =
        '<div class=""><div class="m-2 p-2 text-center under-maintenance-time"><p class="mb-1 fs-12 op-5">DAYS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + d + '</h4></div></div>' +
        '<div class=""><div class="m-2 p-2 text-center under-maintenance-time"><p class="mb-1 fs-12 op-5">HOURS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + h + '</h4></div></div>' +
        '<div class=""><div class="m-2 p-2 text-center under-maintenance-time"><p class="mb-1 fs-12 op-5">MINUTES</p><h4 class="fw-semibold mb-0 text-fixed-white">' + m + '</h4></div></div>' +
        '<div class=""><div class="m-2 p-2 text-center under-maintenance-time"><p class="mb-1 fs-12 op-5">SECONDS</p><h4 class="fw-semibold mb-0 text-fixed-white">' + s + '</h4></div></div>'
}
setInterval('updateTimer()', 1000);