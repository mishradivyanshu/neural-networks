# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 21:57:09 2019

@author: princu
"""

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Python Basics with Numpy (optional assignment)\n",
    "\n",
    "Welcome to your first assignment. This exercise gives you a brief introduction to Python. Even if you've used Python before, this will help familiarize you with functions we'll need.  \n",
    "\n",
    "**Instructions:**\n",
    "- You will be using Python 3.\n",
    "- Avoid using for-loops and while-loops, unless you are explicitly told to do so.\n",
    "- Do not modify the (# GRADED FUNCTION [function name]) comment in some cells. Your work would not be graded if you change this. Each cell containing that comment should only contain one function.\n",
    "- After coding your function, run the cell right below it to check if your result is correct.\n",
    "\n",
    "**After this assignment you will:**\n",
    "- Be able to use iPython Notebooks\n",
    "- Be able to use numpy functions and numpy matrix/vector operations\n",
    "- Understand the concept of \"broadcasting\"\n",
    "- Be able to vectorize code\n",
    "\n",
    "Let's get started!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## About iPython Notebooks ##\n",
    "\n",
    "iPython Notebooks are interactive coding environments embedded in a webpage. You will be using iPython notebooks in this class. You only need to write code between the ### START CODE HERE ### and ### END CODE HERE ### comments. After writing your code, you can run the cell by either pressing \"SHIFT\"+\"ENTER\" or by clicking on \"Run Cell\" (denoted by a play symbol) in the upper bar of the notebook. \n",
    "\n",
    "We will often specify \"(≈ X lines of code)\" in the comments to tell you about how much code you need to write. It is just a rough estimate, so don't feel bad if your code is longer or shorter.\n",
    "\n",
    "**Exercise**: Set test to `\"Hello World\"` in the cell below to print \"Hello World\" and run the two cells below."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "### START CODE HERE ### (≈ 1 line of code)\n",
    "test = None\n",
    "### END CODE HERE ###"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "print (\"test: \" + test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected output**:\n",
    "test: Hello World"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font color='blue'>\n",
    "**What you need to remember**:\n",
    "- Run your cells using SHIFT+ENTER (or \"Run cell\")\n",
    "- Write code in the designated areas using Python 3 only\n",
    "- Do not modify the code outside of the designated areas"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1 - Building basic functions with numpy ##\n",
    "\n",
    "Numpy is the main package for scientific computing in Python. It is maintained by a large community (www.numpy.org). In this exercise you will learn several key numpy functions such as np.exp, np.log, and np.reshape. You will need to know how to use these functions for future assignments.\n",
    "\n",
    "### 1.1 - sigmoid function, np.exp() ###\n",
    "\n",
    "Before using np.exp(), you will use math.exp() to implement the sigmoid function. You will then see why np.exp() is preferable to math.exp().\n",
    "\n",
    "**Exercise**: Build a function that returns the sigmoid of a real number x. Use math.exp(x) for the exponential function.\n",
    "\n",
    "**Reminder**:\n",
    "$sigmoid(x) = \\frac{1}{1+e^{-x}}$ is sometimes also known as the logistic function. It is a non-linear function used not only in Machine Learning (Logistic Regression), but also in Deep Learning.\n",
    "\n",
    "<img src=\"images/Sigmoid.png\" style=\"width:500px;height:228px;\">\n",
    "\n",
    "To refer to a function belonging to a specific package you could call it using package_name.function(). Run the code below to see an example with math.exp()."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: basic_sigmoid\n",
    "\n",
    "import math\n",
    "\n",
    "def basic_sigmoid(x):\n",
    "    \"\"\"\n",
    "    Compute sigmoid of x.\n",
    "\n",
    "    Arguments:\n",
    "    x -- A scalar\n",
    "\n",
    "    Return:\n",
    "    s -- sigmoid(x)\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 1 line of code)\n",
    "    s = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "basic_sigmoid(3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "<table style = \"width:40%\">\n",
    "    <tr>\n",
    "    <td>** basic_sigmoid(3) **</td> \n",
    "        <td>0.9525741268224334 </td> \n",
    "    </tr>\n",
    "\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Actually, we rarely use the \"math\" library in deep learning because the inputs of the functions are real numbers. In deep learning we mostly use matrices and vectors. This is why numpy is more useful. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "### One reason why we use \"numpy\" instead of \"math\" in Deep Learning ###\n",
    "x = [1, 2, 3]\n",
    "basic_sigmoid(x) # you will see this give an error when you run it, because x is a vector."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "In fact, if $ x = (x_1, x_2, ..., x_n)$ is a row vector then $np.exp(x)$ will apply the exponential function to every element of x. The output will thus be: $np.exp(x) = (e^{x_1}, e^{x_2}, ..., e^{x_n})$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "\n",
    "# example of np.exp\n",
    "x = np.array([1, 2, 3])\n",
    "print(np.exp(x)) # result is (exp(1), exp(2), exp(3))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Furthermore, if x is a vector, then a Python operation such as $s = x + 3$ or $s = \\frac{1}{x}$ will output s as a vector of the same size as x."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# example of vector operation\n",
    "x = np.array([1, 2, 3])\n",
    "print (x + 3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Any time you need more info on a numpy function, we encourage you to look at [the official documentation](https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.exp.html). \n",
    "\n",
    "You can also create a new cell in the notebook and write `np.exp?` (for example) to get quick access to the documentation.\n",
    "\n",
    "**Exercise**: Implement the sigmoid function using numpy. \n",
    "\n",
    "**Instructions**: x could now be either a real number, a vector, or a matrix. The data structures we use in numpy to represent these shapes (vectors, matrices...) are called numpy arrays. You don't need to know more for now.\n",
    "$$ \\text{For } x \\in \\mathbb{R}^n \\text{,     } sigmoid(x) = sigmoid\\begin{pmatrix}\n",
    "    x_1  \\\\\n",
    "    x_2  \\\\\n",
    "    ...  \\\\\n",
    "    x_n  \\\\\n",
    "\\end{pmatrix} = \\begin{pmatrix}\n",
    "    \\frac{1}{1+e^{-x_1}}  \\\\\n",
    "    \\frac{1}{1+e^{-x_2}}  \\\\\n",
    "    ...  \\\\\n",
    "    \\frac{1}{1+e^{-x_n}}  \\\\\n",
    "\\end{pmatrix}\\tag{1} $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: sigmoid\n",
    "\n",
    "import numpy as np # this means you can access numpy functions by writing np.function() instead of numpy.function()\n",
    "\n",
    "def sigmoid(x):\n",
    "    \"\"\"\n",
    "    Compute the sigmoid of x\n",
    "\n",
    "    Arguments:\n",
    "    x -- A scalar or numpy array of any size\n",
    "\n",
    "    Return:\n",
    "    s -- sigmoid(x)\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 1 line of code)\n",
    "    s = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = np.array([1, 2, 3])\n",
    "sigmoid(x)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "<table>\n",
    "    <tr> \n",
    "        <td> **sigmoid([1,2,3])**</td> \n",
    "        <td> array([ 0.73105858,  0.88079708,  0.95257413]) </td> \n",
    "    </tr>\n",
    "</table> \n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.2 - Sigmoid gradient\n",
    "\n",
    "As you've seen in lecture, you will need to compute gradients to optimize loss functions using backpropagation. Let's code your first gradient function.\n",
    "\n",
    "**Exercise**: Implement the function sigmoid_grad() to compute the gradient of the sigmoid function with respect to its input x. The formula is: $$sigmoid\\_derivative(x) = \\sigma'(x) = \\sigma(x) (1 - \\sigma(x))\\tag{2}$$\n",
    "You often code this function in two steps:\n",
    "1. Set s to be the sigmoid of x. You might find your sigmoid(x) function useful.\n",
    "2. Compute $\\sigma'(x) = s(1-s)$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: sigmoid_derivative\n",
    "\n",
    "def sigmoid_derivative(x):\n",
    "    \"\"\"\n",
    "    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.\n",
    "    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.\n",
    "    \n",
    "    Arguments:\n",
    "    x -- A scalar or numpy array\n",
    "\n",
    "    Return:\n",
    "    ds -- Your computed gradient.\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 2 lines of code)\n",
    "    s = None\n",
    "    ds = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return ds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = np.array([1, 2, 3])\n",
    "print (\"sigmoid_derivative(x) = \" + str(sigmoid_derivative(x)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "\n",
    "\n",
    "<table>\n",
    "    <tr> \n",
    "        <td> **sigmoid_derivative([1,2,3])**</td> \n",
    "        <td> [ 0.19661193  0.10499359  0.04517666] </td> \n",
    "    </tr>\n",
    "</table> \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.3 - Reshaping arrays ###\n",
    "\n",
    "Two common numpy functions used in deep learning are [np.shape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.shape.html) and [np.reshape()](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html). \n",
    "- X.shape is used to get the shape (dimension) of a matrix/vector X. \n",
    "- X.reshape(...) is used to reshape X into some other dimension. \n",
    "\n",
    "For example, in computer science, an image is represented by a 3D array of shape $(length, height, depth = 3)$. However, when you read an image as the input of an algorithm you convert it to a vector of shape $(length*height*3, 1)$. In other words, you \"unroll\", or reshape, the 3D array into a 1D vector.\n",
    "\n",
    "<img src=\"images/image2vector_kiank.png\" style=\"width:500px;height:300;\">\n",
    "\n",
    "**Exercise**: Implement `image2vector()` that takes an input of shape (length, height, 3) and returns a vector of shape (length\\*height\\*3, 1). For example, if you would like to reshape an array v of shape (a, b, c) into a vector of shape (a*b,c) you would do:\n",
    "``` python\n",
    "v = v.reshape((v.shape[0]*v.shape[1], v.shape[2])) # v.shape[0] = a ; v.shape[1] = b ; v.shape[2] = c\n",
    "```\n",
    "- Please don't hardcode the dimensions of image as a constant. Instead look up the quantities you need with `image.shape[0]`, etc. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: image2vector\n",
    "def image2vector(image):\n",
    "    \"\"\"\n",
    "    Argument:\n",
    "    image -- a numpy array of shape (length, height, depth)\n",
    "    \n",
    "    Returns:\n",
    "    v -- a vector of shape (length*height*depth, 1)\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 1 line of code)\n",
    "    v = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return v"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# This is a 3 by 3 by 2 array, typically images will be (num_px_x, num_px_y,3) where 3 represents the RGB values\n",
    "image = np.array([[[ 0.67826139,  0.29380381],\n",
    "        [ 0.90714982,  0.52835647],\n",
    "        [ 0.4215251 ,  0.45017551]],\n",
    "\n",
    "       [[ 0.92814219,  0.96677647],\n",
    "        [ 0.85304703,  0.52351845],\n",
    "        [ 0.19981397,  0.27417313]],\n",
    "\n",
    "       [[ 0.60659855,  0.00533165],\n",
    "        [ 0.10820313,  0.49978937],\n",
    "        [ 0.34144279,  0.94630077]]])\n",
    "\n",
    "print (\"image2vector(image) = \" + str(image2vector(image)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "\n",
    "\n",
    "<table style=\"width:100%\">\n",
    "     <tr> \n",
    "       <td> **image2vector(image)** </td> \n",
    "       <td> [[ 0.67826139]\n",
    " [ 0.29380381]\n",
    " [ 0.90714982]\n",
    " [ 0.52835647]\n",
    " [ 0.4215251 ]\n",
    " [ 0.45017551]\n",
    " [ 0.92814219]\n",
    " [ 0.96677647]\n",
    " [ 0.85304703]\n",
    " [ 0.52351845]\n",
    " [ 0.19981397]\n",
    " [ 0.27417313]\n",
    " [ 0.60659855]\n",
    " [ 0.00533165]\n",
    " [ 0.10820313]\n",
    " [ 0.49978937]\n",
    " [ 0.34144279]\n",
    " [ 0.94630077]]</td> \n",
    "     </tr>\n",
    "    \n",
    "   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.4 - Normalizing rows\n",
    "\n",
    "Another common technique we use in Machine Learning and Deep Learning is to normalize our data. It often leads to a better performance because gradient descent converges faster after normalization. Here, by normalization we mean changing x to $ \\frac{x}{\\| x\\|} $ (dividing each row vector of x by its norm).\n",
    "\n",
    "For example, if $$x = \n",
    "\\begin{bmatrix}\n",
    "    0 & 3 & 4 \\\\\n",
    "    2 & 6 & 4 \\\\\n",
    "\\end{bmatrix}\\tag{3}$$ then $$\\| x\\| = np.linalg.norm(x, axis = 1, keepdims = True) = \\begin{bmatrix}\n",
    "    5 \\\\\n",
    "    \\sqrt{56} \\\\\n",
    "\\end{bmatrix}\\tag{4} $$and        $$ x\\_normalized = \\frac{x}{\\| x\\|} = \\begin{bmatrix}\n",
    "    0 & \\frac{3}{5} & \\frac{4}{5} \\\\\n",
    "    \\frac{2}{\\sqrt{56}} & \\frac{6}{\\sqrt{56}} & \\frac{4}{\\sqrt{56}} \\\\\n",
    "\\end{bmatrix}\\tag{5}$$ Note that you can divide matrices of different sizes and it works fine: this is called broadcasting and you're going to learn about it in part 5.\n",
    "\n",
    "\n",
    "**Exercise**: Implement normalizeRows() to normalize the rows of a matrix. After applying this function to an input matrix x, each row of x should be a vector of unit length (meaning length 1)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: normalizeRows\n",
    "\n",
    "def normalizeRows(x):\n",
    "    \"\"\"\n",
    "    Implement a function that normalizes each row of the matrix x (to have unit length).\n",
    "    \n",
    "    Argument:\n",
    "    x -- A numpy matrix of shape (n, m)\n",
    "    \n",
    "    Returns:\n",
    "    x -- The normalized (by row) numpy matrix. You are allowed to modify x.\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 2 lines of code)\n",
    "    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord = 2, axis = ..., keepdims = True)\n",
    "    x_norm = None\n",
    "    \n",
    "    # Divide x by its norm.\n",
    "    x = None\n",
    "    ### END CODE HERE ###\n",
    "\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = np.array([\n",
    "    [0, 3, 4],\n",
    "    [1, 6, 4]])\n",
    "print(\"normalizeRows(x) = \" + str(normalizeRows(x)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "\n",
    "<table style=\"width:60%\">\n",
    "\n",
    "     <tr> \n",
    "       <td> **normalizeRows(x)** </td> \n",
    "       <td> [[ 0.          0.6         0.8       ]\n",
    " [ 0.13736056  0.82416338  0.54944226]]</td> \n",
    "     </tr>\n",
    "    \n",
    "   \n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Note**:\n",
    "In normalizeRows(), you can try to print the shapes of x_norm and x, and then rerun the assessment. You'll find out that they have different shapes. This is normal given that x_norm takes the norm of each row of x. So x_norm has the same number of rows but only 1 column. So how did it work when you divided x by x_norm? This is called broadcasting and we'll talk about it now! "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 1.5 - Broadcasting and the softmax function ####\n",
    "A very important concept to understand in numpy is \"broadcasting\". It is very useful for performing mathematical operations between arrays of different shapes. For the full details on broadcasting, you can read the official [broadcasting documentation](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise**: Implement a softmax function using numpy. You can think of softmax as a normalizing function used when your algorithm needs to classify two or more classes. You will learn more about softmax in the second course of this specialization.\n",
    "\n",
    "**Instructions**:\n",
    "- $ \\text{for } x \\in \\mathbb{R}^{1\\times n} \\text{,     } softmax(x) = softmax(\\begin{bmatrix}\n",
    "    x_1  &&\n",
    "    x_2 &&\n",
    "    ...  &&\n",
    "    x_n  \n",
    "\\end{bmatrix}) = \\begin{bmatrix}\n",
    "     \\frac{e^{x_1}}{\\sum_{j}e^{x_j}}  &&\n",
    "    \\frac{e^{x_2}}{\\sum_{j}e^{x_j}}  &&\n",
    "    ...  &&\n",
    "    \\frac{e^{x_n}}{\\sum_{j}e^{x_j}} \n",
    "\\end{bmatrix} $ \n",
    "\n",
    "- $\\text{for a matrix } x \\in \\mathbb{R}^{m \\times n} \\text{,  $x_{ij}$ maps to the element in the $i^{th}$ row and $j^{th}$ column of $x$, thus we have: }$  $$softmax(x) = softmax\\begin{bmatrix}\n",
    "    x_{11} & x_{12} & x_{13} & \\dots  & x_{1n} \\\\\n",
    "    x_{21} & x_{22} & x_{23} & \\dots  & x_{2n} \\\\\n",
    "    \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\\n",
    "    x_{m1} & x_{m2} & x_{m3} & \\dots  & x_{mn}\n",
    "\\end{bmatrix} = \\begin{bmatrix}\n",
    "    \\frac{e^{x_{11}}}{\\sum_{j}e^{x_{1j}}} & \\frac{e^{x_{12}}}{\\sum_{j}e^{x_{1j}}} & \\frac{e^{x_{13}}}{\\sum_{j}e^{x_{1j}}} & \\dots  & \\frac{e^{x_{1n}}}{\\sum_{j}e^{x_{1j}}} \\\\\n",
    "    \\frac{e^{x_{21}}}{\\sum_{j}e^{x_{2j}}} & \\frac{e^{x_{22}}}{\\sum_{j}e^{x_{2j}}} & \\frac{e^{x_{23}}}{\\sum_{j}e^{x_{2j}}} & \\dots  & \\frac{e^{x_{2n}}}{\\sum_{j}e^{x_{2j}}} \\\\\n",
    "    \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\\n",
    "    \\frac{e^{x_{m1}}}{\\sum_{j}e^{x_{mj}}} & \\frac{e^{x_{m2}}}{\\sum_{j}e^{x_{mj}}} & \\frac{e^{x_{m3}}}{\\sum_{j}e^{x_{mj}}} & \\dots  & \\frac{e^{x_{mn}}}{\\sum_{j}e^{x_{mj}}}\n",
    "\\end{bmatrix} = \\begin{pmatrix}\n",
    "    softmax\\text{(first row of x)}  \\\\\n",
    "    softmax\\text{(second row of x)} \\\\\n",
    "    ...  \\\\\n",
    "    softmax\\text{(last row of x)} \\\\\n",
    "\\end{pmatrix} $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: softmax\n",
    "\n",
    "def softmax(x):\n",
    "    \"\"\"Calculates the softmax for each row of the input x.\n",
    "\n",
    "    Your code should work for a row vector and also for matrices of shape (n, m).\n",
    "\n",
    "    Argument:\n",
    "    x -- A numpy matrix of shape (n,m)\n",
    "\n",
    "    Returns:\n",
    "    s -- A numpy matrix equal to the softmax of x, of shape (n,m)\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 3 lines of code)\n",
    "    # Apply exp() element-wise to x. Use np.exp(...).\n",
    "    x_exp = None\n",
    "\n",
    "    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True).\n",
    "    x_sum = None\n",
    "    \n",
    "    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting.\n",
    "    s = None\n",
    "\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x = np.array([\n",
    "    [9, 2, 5, 0, 0],\n",
    "    [7, 5, 0, 0 ,0]])\n",
    "print(\"softmax(x) = \" + str(softmax(x)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**:\n",
    "\n",
    "<table style=\"width:60%\">\n",
    "\n",
    "     <tr> \n",
    "       <td> **softmax(x)** </td> \n",
    "       <td> [[  9.80897665e-01   8.94462891e-04   1.79657674e-02   1.21052389e-04\n",
    "    1.21052389e-04]\n",
    " [  8.78679856e-01   1.18916387e-01   8.01252314e-04   8.01252314e-04\n",
    "    8.01252314e-04]]</td> \n",
    "     </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Note**:\n",
    "- If you print the shapes of x_exp, x_sum and s above and rerun the assessment cell, you will see that x_sum is of shape (2,1) while x_exp and s are of shape (2,5). **x_exp/x_sum** works due to python broadcasting.\n",
    "\n",
    "Congratulations! You now have a pretty good understanding of python numpy and have implemented a few useful functions that you will be using in deep learning."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font color='blue'>\n",
    "**What you need to remember:**\n",
    "- np.exp(x) works for any np.array x and applies the exponential function to every coordinate\n",
    "- the sigmoid function and its gradient\n",
    "- image2vector is commonly used in deep learning\n",
    "- np.reshape is widely used. In the future, you'll see that keeping your matrix/vector dimensions straight will go toward eliminating a lot of bugs. \n",
    "- numpy has efficient built-in functions\n",
    "- broadcasting is extremely useful"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## 2) Vectorization"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "In deep learning, you deal with very large datasets. Hence, a non-computationally-optimal function can become a huge bottleneck in your algorithm and can result in a model that takes ages to run. To make sure that your code is  computationally efficient, you will use vectorization. For example, try to tell the difference between the following implementations of the dot/outer/elementwise product."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "import time\n",
    "\n",
    "x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]\n",
    "x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]\n",
    "\n",
    "### CLASSIC DOT PRODUCT OF VECTORS IMPLEMENTATION ###\n",
    "tic = time.process_time()\n",
    "dot = 0\n",
    "for i in range(len(x1)):\n",
    "    dot+= x1[i]*x2[i]\n",
    "toc = time.process_time()\n",
    "print (\"dot = \" + str(dot) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### CLASSIC OUTER PRODUCT IMPLEMENTATION ###\n",
    "tic = time.process_time()\n",
    "outer = np.zeros((len(x1),len(x2))) # we create a len(x1)*len(x2) matrix with only zeros\n",
    "for i in range(len(x1)):\n",
    "    for j in range(len(x2)):\n",
    "        outer[i,j] = x1[i]*x2[j]\n",
    "toc = time.process_time()\n",
    "print (\"outer = \" + str(outer) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### CLASSIC ELEMENTWISE IMPLEMENTATION ###\n",
    "tic = time.process_time()\n",
    "mul = np.zeros(len(x1))\n",
    "for i in range(len(x1)):\n",
    "    mul[i] = x1[i]*x2[i]\n",
    "toc = time.process_time()\n",
    "print (\"elementwise multiplication = \" + str(mul) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### CLASSIC GENERAL DOT PRODUCT IMPLEMENTATION ###\n",
    "W = np.random.rand(3,len(x1)) # Random 3*len(x1) numpy array\n",
    "tic = time.process_time()\n",
    "gdot = np.zeros(W.shape[0])\n",
    "for i in range(W.shape[0]):\n",
    "    for j in range(len(x1)):\n",
    "        gdot[i] += W[i,j]*x1[j]\n",
    "toc = time.process_time()\n",
    "print (\"gdot = \" + str(gdot) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "x1 = [9, 2, 5, 0, 0, 7, 5, 0, 0, 0, 9, 2, 5, 0, 0]\n",
    "x2 = [9, 2, 2, 9, 0, 9, 2, 5, 0, 0, 9, 2, 5, 0, 0]\n",
    "\n",
    "### VECTORIZED DOT PRODUCT OF VECTORS ###\n",
    "tic = time.process_time()\n",
    "dot = np.dot(x1,x2)\n",
    "toc = time.process_time()\n",
    "print (\"dot = \" + str(dot) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### VECTORIZED OUTER PRODUCT ###\n",
    "tic = time.process_time()\n",
    "outer = np.outer(x1,x2)\n",
    "toc = time.process_time()\n",
    "print (\"outer = \" + str(outer) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### VECTORIZED ELEMENTWISE MULTIPLICATION ###\n",
    "tic = time.process_time()\n",
    "mul = np.multiply(x1,x2)\n",
    "toc = time.process_time()\n",
    "print (\"elementwise multiplication = \" + str(mul) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")\n",
    "\n",
    "### VECTORIZED GENERAL DOT PRODUCT ###\n",
    "tic = time.process_time()\n",
    "dot = np.dot(W,x1)\n",
    "toc = time.process_time()\n",
    "print (\"gdot = \" + str(dot) + \"\\n ----- Computation time = \" + str(1000*(toc - tic)) + \"ms\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "As you may have noticed, the vectorized implementation is much cleaner and more efficient. For bigger vectors/matrices, the differences in running time become even bigger. \n",
    "\n",
    "**Note** that `np.dot()` performs a matrix-matrix or matrix-vector multiplication. This is different from `np.multiply()` and the `*` operator (which is equivalent to  `.*` in Matlab/Octave), which performs an element-wise multiplication."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 2.1 Implement the L1 and L2 loss functions\n",
    "\n",
    "**Exercise**: Implement the numpy vectorized version of the L1 loss. You may find the function abs(x) (absolute value of x) useful.\n",
    "\n",
    "**Reminder**:\n",
    "- The loss is used to evaluate the performance of your model. The bigger your loss is, the more different your predictions ($ \\hat{y} $) are from the true values ($y$). In deep learning, you use optimization algorithms like Gradient Descent to train your model and to minimize the cost.\n",
    "- L1 loss is defined as:\n",
    "$$\\begin{align*} & L_1(\\hat{y}, y) = \\sum_{i=0}^m|y^{(i)} - \\hat{y}^{(i)}| \\end{align*}\\tag{6}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: L1\n",
    "\n",
    "def L1(yhat, y):\n",
    "    \"\"\"\n",
    "    Arguments:\n",
    "    yhat -- vector of size m (predicted labels)\n",
    "    y -- vector of size m (true labels)\n",
    "    \n",
    "    Returns:\n",
    "    loss -- the value of the L1 loss function defined above\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 1 line of code)\n",
    "    loss = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "yhat = np.array([.9, 0.2, 0.1, .4, .9])\n",
    "y = np.array([1, 0, 0, 1, 1])\n",
    "print(\"L1 = \" + str(L1(yhat,y)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**:\n",
    "\n",
    "<table style=\"width:20%\">\n",
    "\n",
    "     <tr> \n",
    "       <td> **L1** </td> \n",
    "       <td> 1.1 </td> \n",
    "     </tr>\n",
    "</table>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Exercise**: Implement the numpy vectorized version of the L2 loss. There are several way of implementing the L2 loss but you may find the function np.dot() useful. As a reminder, if $x = [x_1, x_2, ..., x_n]$, then `np.dot(x,x)` = $\\sum_{j=0}^n x_j^{2}$. \n",
    "\n",
    "- L2 loss is defined as $$\\begin{align*} & L_2(\\hat{y},y) = \\sum_{i=0}^m(y^{(i)} - \\hat{y}^{(i)})^2 \\end{align*}\\tag{7}$$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# GRADED FUNCTION: L2\n",
    "\n",
    "def L2(yhat, y):\n",
    "    \"\"\"\n",
    "    Arguments:\n",
    "    yhat -- vector of size m (predicted labels)\n",
    "    y -- vector of size m (true labels)\n",
    "    \n",
    "    Returns:\n",
    "    loss -- the value of the L2 loss function defined above\n",
    "    \"\"\"\n",
    "    \n",
    "    ### START CODE HERE ### (≈ 1 line of code)\n",
    "    loss = None\n",
    "    ### END CODE HERE ###\n",
    "    \n",
    "    return loss"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "yhat = np.array([.9, 0.2, 0.1, .4, .9])\n",
    "y = np.array([1, 0, 0, 1, 1])\n",
    "print(\"L2 = \" + str(L2(yhat,y)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Expected Output**: \n",
    "<table style=\"width:20%\">\n",
    "     <tr> \n",
    "       <td> **L2** </td> \n",
    "       <td> 0.43 </td> \n",
    "     </tr>\n",
    "</table>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Congratulations on completing this assignment. We hope that this little warm-up exercise helps you in the future assignments, which will be more exciting and interesting!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<font color='blue'>\n",
    "**What to remember:**\n",
    "- Vectorization is very important in deep learning. It provides computational efficiency and clarity.\n",
    "- You have reviewed the L1 and L2 loss.\n",
    "- You are familiar with many numpy functions such as np.sum, np.dot, np.multiply, np.maximum, etc..."
   ]
  }
 ],
 "metadata": {
  "coursera": {
   "course_slug": "neural-networks-deep-learning",
   "graded_item_id": "XHpfv",
   "launcher_item_id": "Zh0CU"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
