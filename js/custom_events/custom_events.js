// 
// Copied from https://stackoverflow.com/questions/15308371/custom-events-model-without-using-dom-events-in-javascript
//

var MyEventTarget = function(options) {
    // Create a DOM EventTarget object
    var target = document.createTextNode(null);

    // Pass EventTarget interface calls to DOM EventTarget object
    this.addEventListener = target.addEventListener.bind(target);
    this.removeEventListener = target.removeEventListener.bind(target);
    this.dispatchEvent = target.dispatchEvent.bind(target);

    // Room your your constructor code 
}

// Create an instance of your event target
myTarget = new MyEventTarget();

// Add an event listener to your event target
myTarget.addEventListener("myevent", function(){alert("hello")});

// Dispatch an event from your event target
var evt = new Event('myevent');
myTarget.dispatchEvent(evt);
