document.addEventListener('DOMContentLoaded', () => {
  let appTitle = document.getElementById('app-title');
  let appDescription = document.getElementById('app-description');
  let appUrl = document.getElementById('app-url');
  let appSubmit = document.getElementById('app-submit');
  let loginLogout = document.getElementById('header-login-logout')

  // Firebase初期化
  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyD_chE56aSAaeJrZsKmrW_TmrFLi0V9S8s",
    authDomain: "bifb-7e009.firebaseapp.com",
    projectId: "bifb-7e009",
    storageBucket: "bifb-7e009.appspot.com",
    messagingSenderId: "839728206726",
    appId: "1:839728206726:web:fb4ff2f60ece9e3b785207",
    measurementId: "G-C0KD1176QH"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();
  // Initialize the FirebaseUI Widget using Firebase.
  const uiConfig = {
      callbacks: {
        signInSuccessWithAuthResult: function(authResult, redirectUrl) {
          // User successfully signed in.
          // Return type determines whether we continue the redirect automatically
          // or whether we leave that to developer to handle.
          return true;
        },
        uiShown: function() {
          // The widget is rendered.
          // Hide the loader.
          document.getElementById('loader').style.display = 'none';
        }
      },
      // Will use popup for IDP Providers sign-in flow instead of the default, redirect.
      signInFlow: 'popup',
      signInSuccessUrl: '/',
      signInOptions: [
        // Leave the lines as is for the providers you want to offer your users.
        firebase.auth.GoogleAuthProvider.PROVIDER_ID,
      ],
  };
  // The start method will wait until the DOM is loaded.
  if (location.pathname === '/login') {
    const ui = new firebaseui.auth.AuthUI(firebase.auth());
    ui.start('#firebaseui-auth-container', uiConfig);
  }
  
  firebase.auth().onAuthStateChanged((user) => {
    if (user) {
      // User is signed in, see docs for a list of available properties
      // https://firebase.google.com/docs/reference/js/firebase.User
      loginLogout.textContent = 'ログアウト';
      const userData = JSON.stringify({'user_id': user.uid, 'user_name': user.displayName, 'email': user.email})
      $.ajax({
        type: 'POST',
        url: '/user/add',
        data: userData,
        contentType: 'application/json',
        success: function(data) {
          // console.log(data);
        },
        error: function(error) {
          // console.log(error)
        }
      })
    } else {
      // User is signed out
      if (location.pathname !== '/login'){
        window.location.href = '/login';
      }
    }
  });

  loginLogout.addEventListener('click', ()=> {
    if (loginLogout.textContent === 'ログアウト'){
      firebase.auth().signOut().then(function() {
        // alert('ログアウト成功')
      }).catch(function(error) {
        // alert('ログアウト失敗')
      })
    }
  }, false);

  if (location.pathname === '/post') {
    appSubmit.addEventListener('click', () => {
      let user = firebase.auth().currentUser;
      if (user !== null) {
        let data = {"app_title": appTitle.value, "app_description": appDescription.value, "app_url": appUrl.value, "user_id": user.uid};
        post('/post/try', data)
      }
    }, false);
  }


  // 無理やりPOSTするための関数
  function post(path, params, method='post') {
    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;
  
    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
  
        form.appendChild(hiddenField);
      }
    }
  
    document.body.appendChild(form);
    form.submit();
  }
}, false)