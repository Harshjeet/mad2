export default {
    template: `
    <div class="d-flex justify-content-center" style ="margin-top: 15vh">

        <div class = "mb-3 p-5 bg-light">
        <h3> USER LOGIN FORM </h3>
        <br>
        
            <form>
                <!-- Email input -->
                <div class="form-outline mb-4">
                <input type="email" id="user-email" class="form-control" v-model = "login_cred.email"/>
                <label class="form-label" for="user-email">Email address</label>
                
                </div>
            
                <!-- Password input -->
                <div class="form-outline mb-4">
                <input type="password" id="user-password" class="form-control" v-model = "login_cred.password" />
                <label class="form-label" for="user-password">Password</label>
                
                </div>
            
                <!-- 2 column grid layout for inline styling -->
                <div class="row mb-4">
                <div class="col d-flex justify-content-center">
                    <!-- Checkbox -->
                    <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="user-checkbox" checked />
                    <label class="form-check-label" for="user-checkbox"> Remember me </label>
                    </div>
                </div>
                </div>
            
                <!-- Submit button -->
                <button class="btn btn-primary btn-block mb-4" @user_click_login>Sign in</button>

            </form>
        </div>
    </div>
    `,

    data() {
        return {
            login_cred: {
                email: '',
                password: ''
            },
        }
    }, 

    methods: {

        async user_click_login() {
            console.log(this.login_cred)
        }
    }
}

