document.addEventListener("DOMContentLoaded", function () {

    // ========================================================
    // CSRF TOKEN
    // ========================================================

    function getCookie(name) {

        let cookieValue = null;

        if (document.cookie && document.cookie !== "") {

            const cookies = document.cookie.split(";");

            for (let cookie of cookies) {

                cookie = cookie.trim();

                if (
                    cookie.substring(0, name.length + 1) ===
                    name + "="
                ) {

                    cookieValue = decodeURIComponent(
                        cookie.substring(name.length + 1)
                    );

                    break;
                }
            }
        }

        return cookieValue;
    }


    const csrftoken = getCookie("csrftoken");


    // ========================================================
    // LIKE SYSTEM
    // ========================================================

    document.querySelectorAll(".like-btn").forEach(
        function (button) {

            button.addEventListener("click", function () {

                const postId =
                    button.dataset.postId;

                const currentPosition =
                    window.scrollY;


                fetch(
                    `/post/${postId}/like/`,
                    {
                        method: "POST",

                        headers: {
                            "X-CSRFToken": csrftoken,
                            "X-Requested-With": "XMLHttpRequest",
                        },
                    }
                )
                .then(response => response.json())

                .then(data => {

                    if (!data.success) {
                        return;
                    }


                    const countElement =
                        document.getElementById(
                            `likes-count-${postId}`
                        );


                    if (countElement) {

                        countElement.textContent =
                            `${data.likes_count} likes`;
                    }


                    const icon =
                        button.querySelector(
                            ".like-icon"
                        );


                    if (data.liked) {

                        button.classList.add(
                            "liked"
                        );

                        if (icon) {
                            icon.textContent = "♥";
                        }

                    } else {

                        button.classList.remove(
                            "liked"
                        );

                        if (icon) {
                            icon.textContent = "♡";
                        }
                    }


                    // Prevent scroll jump
                    window.scrollTo(
                        0,
                        currentPosition
                    );

                })

                .catch(error => {
                    console.error(error);
                });

            });

        }
    );


    // ========================================================
    // COMMENT SYSTEM
    // ========================================================

    document.querySelectorAll(".comment-form").forEach(
        function (form) {

            form.addEventListener(
                "submit",
                function (event) {

                    event.preventDefault();


                    const postId =
                        form.dataset.postId;

                    const input =
                        form.querySelector(
                            "input[name='text']"
                        );

                    const text =
                        input.value.trim();


                    if (!text) {
                        return;
                    }


                    const currentPosition =
                        window.scrollY;


                    const formData =
                        new FormData();

                    formData.append(
                        "text",
                        text
                    );


                    fetch(
                        `/post/${postId}/comment/`,
                        {
                            method: "POST",

                            headers: {
                                "X-CSRFToken": csrftoken,
                                "X-Requested-With": "XMLHttpRequest",
                            },

                            body: formData,
                        }
                    )

                    .then(response =>
                        response.json()
                    )

                    .then(data => {

                        if (!data.success) {
                            return;
                        }


                        const commentsList =
                            document.getElementById(
                                `comments-list-${postId}`
                            );


                        const comment =
                            document.createElement(
                                "div"
                            );

                        comment.className =
                            "comment new-comment";


                        comment.innerHTML = `

                            <div class="tiny-avatar avatar-placeholder">
                                ${data.comment.author
                                    .charAt(0)
                                    .toUpperCase()}
                            </div>

                            <div class="comment-body">

                                <strong>
                                    @${escapeHtml(
                                        data.comment.author
                                    )}
                                </strong>

                                <p>
                                    ${escapeHtml(
                                        data.comment.text
                                    )}
                                </p>

                                <small>
                                    Just now
                                </small>

                            </div>
                        `;


                        commentsList.appendChild(
                            comment
                        );


                        input.value = "";


                        const countElement =
                            document.getElementById(
                                `comments-count-${postId}`
                            );


                        if (countElement) {

                            countElement.textContent =
                                `${data.comments_count} comments`;
                        }


                        // Keep same scroll position
                        window.scrollTo(
                            0,
                            currentPosition
                        );

                    })

                    .catch(error => {
                        console.error(error);
                    });

                }
            );

        }
    );


    // ========================================================
    // FOLLOW SYSTEM
    // ========================================================

    document.querySelectorAll(".follow-btn").forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    const username =
                        button.dataset.username;

                    const currentPosition =
                        window.scrollY;


                    fetch(
                        `/profile/${encodeURIComponent(username)}/follow/`,
                        {
                            method: "POST",

                            headers: {
                                "X-CSRFToken": csrftoken,
                                "X-Requested-With": "XMLHttpRequest",
                            },
                        }
                    )

                    .then(response =>
                        response.json()
                    )

                    .then(data => {

                        if (!data.success) {
                            return;
                        }


                        button.textContent =
                            data.following
                                ? "Following"
                                : "Follow";


                        const followers =
                            document.getElementById(
                                "profile-followers-count"
                            );


                        if (followers) {

                            followers.textContent =
                                data.followers_count;
                        }


                        window.scrollTo(
                            0,
                            currentPosition
                        );

                    })

                    .catch(error => {
                        console.error(error);
                    });

                }
            );

        }
    );


    // ========================================================
    // COMMENT BUTTON
    // ========================================================

    document.querySelectorAll(
        ".comment-focus-btn"
    ).forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    const postId =
                        button.dataset.postId;

                    const form =
                        document.querySelector(
                            `.comment-form[data-post-id="${postId}"]`
                        );


                    if (form) {

                        const input =
                            form.querySelector(
                                "input"
                            );

                        input.focus();
                    }

                }
            );

        }
    );


    // ========================================================
    // IMAGE PREVIEW
    // ========================================================

    const imageInput =
        document.getElementById(
            "post-images"
        );

    const preview =
        document.getElementById(
            "image-preview"
        );


    if (imageInput && preview) {

        imageInput.addEventListener(
            "change",
            function () {

                preview.innerHTML = "";


                Array.from(
                    imageInput.files
                ).forEach(
                    function (file) {

                        if (
                            !file.type.startsWith(
                                "image/"
                            )
                        ) {
                            return;
                        }


                        const reader =
                            new FileReader();


                        reader.onload =
                            function (event) {

                                const img =
                                    document.createElement(
                                        "img"
                                    );

                                img.src =
                                    event.target.result;

                                preview.appendChild(
                                    img
                                );
                            };


                        reader.readAsDataURL(
                            file
                        );

                    }
                );

            }
        );

    }


    // ========================================================
    // DELETE POST
    // ========================================================

    document.querySelectorAll(
        ".delete-post-btn"
    ).forEach(
        function (button) {

            button.addEventListener(
                "click",
                function () {

                    const postId =
                        button.dataset.postId;


                    if (
                        !confirm(
                            "Delete this post?"
                        )
                    ) {
                        return;
                    }


                    fetch(
                        `/post/${postId}/delete/`,
                        {
                            method: "POST",

                            headers: {
                                "X-CSRFToken": csrftoken,
                                "X-Requested-With": "XMLHttpRequest",
                            },
                        }
                    )

                    .then(response =>
                        response.json()
                    )

                    .then(data => {

                        if (data.success) {

                            const post =
                                document.getElementById(
                                    `post-${postId}`
                                );


                            if (post) {
                                post.remove();
                            }
                        }

                    })

                    .catch(error => {
                        console.error(error);
                    });

                }
            );

        }
    );


    // ========================================================
    // HTML ESCAPE
    // Prevent unsafe HTML injection in AJAX comments
    // ========================================================

    function escapeHtml(text) {

        const div =
            document.createElement("div");

        div.textContent = text;

        return div.innerHTML;
    }

});