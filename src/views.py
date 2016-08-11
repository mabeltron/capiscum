def login():
    from forms import LoginForm
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)
