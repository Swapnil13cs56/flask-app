from flask import render_template, url_for, flash, redirect, request
from werkzeug.utils import html
from swapnilblog import app, db
from swapnilblog.forms import PostForm
from swapnilblog.models import Post
from sqlalchemy import func


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/blog/medium")
def medium():
    return render_template('medium.html', title='medium')

@app.route("/blog")
def blog():
    posts = Post.query.filter(Post.category == 'general')
    return render_template('blog.html', title='blog', posts=posts)

@app.route("/devops")
def devops():
    posts = Post.query.filter(Post.category == 'devops')
    return render_template('devops.html', title='devops', posts=posts)

@app.route("/azure")
def azure():
    posts = Post.query.filter(Post.category == 'azure')
    return render_template('azure.html', title='azure', posts=posts)

@app.route("/software-testing")
def software_testing():
    posts = Post.query.filter(Post.category == 'software testing')
    return render_template('software-testing.html', title='software testing', posts=posts)

@app.route("/personal-growth")
def personal_growth():
    posts = Post.query.filter(Post.category == 'personal growth')
    return render_template('personal-growth.html', title='personal growth', posts=posts)

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='gallery')

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author="Swapnil", category=func.lower(form.category.data))
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='new post', form=form, legend='new post')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='post.title', post=post)

@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('post updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='update post', form=form, legend='update post')

@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('post deleted!', 'success')
    return redirect(url_for('home'))

@app.route("/custom")
def custom():
    return render_template('custom.html', posts=posts, title='custom')

