# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user

from micro_blog.extensions import login_manager
from micro_blog.public.forms import LoginForm
from micro_blog.user.forms import RegisterForm
from micro_blog.user.models import User
from micro_blog.utils import flash_errors

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route("/", methods=["GET", "POST"])
def home():
    """Home page."""
    form = LoginForm(request.form)
    if request.method == "POST":
        # TODO: CSRF token is bad, add log in logic
        print(entry_content)
        if form.validate_on_submit():
            login_user(form.user)
            flash("You are logged in.", "success")
            redirect_url = request.args.get("next") or url_for("user.members")
            return redirect(redirect_url)
        else:
            flash_errors(form)
        isLoggenIn = False # TODO: make this work
        if isLoggedIn:
            current_app.logger.info("POST")
            entry_content = request.form.get("content")
            
    return render_template("public/home.html", form=form)


@blueprint.route("/logout/")
@login_required
def logout():
    """Logout."""
    logout_user()
    flash("You are logged out.", "info")
    return redirect(url_for("public.home"))


@blueprint.route("/register/", methods=["GET", "POST"])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
            active=True,
        )
        flash("Thank you for registering. You can now log in.", "success")
        return redirect(url_for("public.home"))
    else:
        flash_errors(form)
    return render_template("public/register.html", form=form)


@blueprint.route("/about/")
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/about.html", form=form)

@blueprint.route("/recent/")
def recent():
    """About page."""
    form = LoginForm(request.form)
    return render_template("public/recent.html", form=form)
    
@blueprint.route("/portfolio/")
def portfolio():
    """Portfolio page."""
    form = LoginForm(request.form)
    return render_template("public/portfolio.html", form=form)
    
@blueprint.route("/Calendar/")
def Calendar():
    """Calendar page."""
    form = LoginForm(request.form)
    return render_template("public/Calendar.html", form=form)