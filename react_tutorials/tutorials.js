import React from "react"
import ReactDOM from "react-dom";

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return 'You liked this.';
    }

    return (
        <button className='button' onClick={() => this.setState({liked: true})}>
            Like
        </button>
    );
  }
}

class Clock extends React.Component {

    constructor(props) {
        super(props);
        this.state = {date: new Date()};
    }

    tick() {
        this.setState({date: new Date()});
    }

    componentDidMount() {
        this.timerId = setInterval(() => this.tick(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.timerId);
    }

    render() {
        return (
            <div>
                <h2> This is {this.state.date.toLocaleTimeString()}.</h2>
            </div>
        )
    }
}

function UserGreeting(props){
    return <h2>Wellcome Back.</h2>
}

function GuestGreeting(props) {
    return <h2>Please sign up.</h2>
}

function Greeting(props) {
    const isLoggedIn = props.isLoggedIn;
    if (isLoggedIn) {
        return <UserGreeting />;
    } else {
        return <GuestGreeting />;
    }
}

function LoginButton(props) {
    return (
        <button onClick={props.onClick}>
            Login
        </button>
    )
}

function LogoutButton(props) {
    return (
        <button onClick={props.onClick}>
            Log out
        </button>
    )
}


class LoginControl extends React.Component {

    constructor(props){
        super(props);
        this.handleLoginClick = this.handleLoginClick.bind(this);
        this.handleLogoutClick = this.handleLogoutClick.bind(this);
        this.state = {isLoggedIn: false};
    }

    handleLoginClick() {
        this.setState({isLoggedIn: true});
    }

    handleLogoutClick() {
        this.setState({isLoggedIn: false});
    }

    render() {
        const isLoggedIn = this.state.isLoggedIn;
        let button;

        if (isLoggedIn) {
            button =  <LogoutButton onClick={this.handleLogoutClick}/>
        } else {
            button = <LoginButton onClick={this.handleLoginClick}/>
        }

        return (
            <div>
                <Greeting isLoggedIn={isLoggedIn}/>
                {button}
            </div>
        )
    }
}


class NameForm extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.state = {value: ''}
    }

    handleChange(event) {
        this.setState({value: event.target.value.toUpperCase()});
    }

    handleSubmit(event) {
        alert('A name was submited: ' + this.state.value);
        event.preventDefault();
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <label>
                    Name:
                    <input className='input' value={this.state.value} onChange={this.handleChange}/>
                </label>
                <input type="submit" value="Submit"/>
            </form>
        )
    }
}


class EachInput extends React.Component {

    render() {
        return (
            <div id={this.props.value}>
                <h3>Name</h3>
                <input className='input' />
            </div>
        )
    }
}

class AddMore extends React.Component {
    render() {
        return (
            <div>
                <button onClick={this.props.onClick}> + </button>
            </div>
        )
    }
}


class AppInput extends React.Component {

    constructor(props) {
        super(props);
        this.addMoreInput = this.addMoreInput.bind(this);
        this.state = {
            'listItems': [0]
        };
    }

    addMoreInput() {
        this.setState(function(prelist, props) {
            return {
                listItems: prelist.listItems.concat(prelist.listItems.length)
            };
        });
    }

    render() {
        let listItems;

        listItems = this.state.listItems.map((number) => <EachInput key={number.toString()} value={number} />);
        return (
            <div>
                <form>
                    {listItems}
                    <input type="submit" value="Submit"/>
                </form>
                <AddMore onClick={this.addMoreInput}/>
            </div>
        )
    }
}


function App() {

    return (
        <div>
            <div>
                <LikeButton />
            </div>
            <div>
                <Clock />
            </div>
            <div>
                <LoginControl />
            </div>
            <div>
                <AppInput />
            </div>
        </div>
    );
}


ReactDOM.render(<App />, document.getElementById('react_container'));