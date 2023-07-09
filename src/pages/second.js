document.addEventListener('DOMContentLoaded', function() {
console.log('hello world')
        const form = document.getElementById('form');
        // const formDate = new FormData(form);


        document.getElementById('btn_submit').addEventListener("click", function(event) {
            event.preventDefault(); // Prevent the form from submitting normally

            const formDate = new FormData(form);
            username = document.getElementById('floatingInput').value.toLowerCase()
            password  = document.getElementById('floatingPassword').value

            data = {
                'username':username,
                'password':password
            }

            console.log(data)
            console.log(formDate)

            fetch('http://127.0.0.1:8000/auth/jwt/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(function(response) {
                console.log('sussssceee')
                console.log(JSON.stringify(data))

                if (response.status === 204) {
                    window.location.href = 'http://localhost:8000/docs'; // Redirect to success page
                } else {
                    console.log('total error', response.status)
                    console.log(formDate)
                    console.log(JSON.stringify(data))
                    // Handle other response statuses or errors
                }
            })
            .catch(function(error) {
                console.log('Total error sorry ')
            });
        });
    });