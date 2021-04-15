let counter = 0;
var stop = false;
const quantity = 5;

document.addEventListener('DOMContentLoaded', load);

window.onscroll = () => {
    if (stop == false) {
        if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
            load();
        }
    }
};

function load() {

    const start = counter;
    const end = start + quantity - 1;
    counter = end + 1;
    stop = true;
    fetch(`/bookpaths?start=${start}&end=${end}`)
        .then(response => response.json())
        .then(data => {
            var content = JSON.parse(data.bookpaths);
            if (content.length != 0) {
                content.forEach(add_post);
                stop = false;
            }
        })
};

function add_post(contents) {

    const media_div = document.createElement('div');
    media_div.className = "media container position-relative bg-light shadow p-4 rounded mb-3";

    const body_div = document.createElement('div');
    body_div.className = 'media-body';

    const name_h3 = document.createElement('h3');
    name_h3.innerHTML = contents.fields.name;
    body_div.appendChild(name_h3);

    const category_span = document.createElement('span');
    category_span.className = 'text-muted d-block';
    category_span.innerHTML = 'Category: ' + contents.fields.category;
    body_div.appendChild(category_span);

    const description_span = document.createElement('span');
    description_span.className = 'text-muted d-block';
    description_span.innerHTML = contents.fields.description;
    body_div.appendChild(description_span);

    const followers_span = document.createElement('span');
    followers_span.className = 'd-block';
    followers_span.innerHTML = 'Followers: ' + contents.fields.follow_count;
    body_div.appendChild(followers_span);

    const bookpath_link = document.createElement('a');
    bookpath_link.className = 'stretched-link';
    bookpath_link.href = 'bookpath/' + contents.pk;
    body_div.appendChild(bookpath_link);

    media_div.appendChild(body_div)
    document.querySelector('#bookpaths').append(media_div);
};

