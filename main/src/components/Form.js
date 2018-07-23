import React, {Component} from "react"
import PropTypes from "prop-types"


class Form extends Component {

    static propTypes = {
        endpoint: PropTypes.string.isRequired
    };

    state = {
        title: '',
        code: ''
    };

    handleChange = e => {
        this.setState({[e.target.name]: e.target.value});
    };

    handleSubmit = e => {

        e.preventDefault();
        const {title, code} = this.state;
        const snippet = {title, code};
        const conf = {
            method: 'post',
            body: JSON.stringify(snippet),
            headers: new Headers({"Content-Type": 'application/json'})
        };
        fetch(this.props.endpoint, conf).then(response => console.log(response));
    };

    render() {

        const {title, code} = this.state;
        return (

            <div className="column">
                <form className="reactjs-form" onSubmit={this.handleSubmit}>
                    <div className="field">
                        <label className="label">Title</label>
                        <div className="control">
                            <input
                                className="input"
                                type="text"
                                name="title"
                                onChange={this.handleChange}
                                value={title}
                                required
                            />
                        </div>
                    </div>
                    <div className="field">
                        <label className="label">Code</label>
                        <div className="control">
                            <input
                                className="input"
                                type="text"
                                name="code"
                                onChange={this.handleChange}
                                value={code}
                                required
                            />
                        </div>
                    </div>
                    <div className="control">
                        <button type="submit" name="reactjs-submit" className="button is-info">
                            Send Snippet
                        </button>
                    </div>
                </form>
            </div>
        );
    }
}

export default Form;