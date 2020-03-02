# wi-contouring

##Installation
* Setup development environment

```bash
cd wi-contouring
python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

* Start the service

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:app
```

* API will be accessible at localhost:5000/kriging. Your request must contains json object like this:

```
{
	"x": [0.1, 0.2, 0.3],
	"y": [1.4, 1.5, 1.6],
	"z": [1, 0.5, 0.6],
	"x_start": 1,
	"x_stop": 2,
	"x_step": 0.1,
	"y_start": 1,
	"y_stop": 2,
	"y_step": 0.1
}
```
The response will be a 2-dimensional array which present predicted values at given grid:

```
[[0.74362416 0.6676064 0.66308837 0.71264335 0.76156368 0.78440582
0.78918628 0.78867905 0.78803123 0.78782089]
[0.70919422 0.67540596 0.70173061 0.74857558 0.77868702 0.78828219
0.78893869 0.78821268 0.78787061 0.78778893]
[0.70028079 0.70123265 0.73749844 0.77114144 0.78612796 0.78893955
0.78843005 0.78795363 0.78780626 0.78777871]
[0.71149016 0.73153689 0.76319149 0.78260861 0.78841577 0.78861172
0.78807225 0.78783817 0.787784 0.78777583]
[0.73255891 0.7568596 0.77813006 0.78715337 0.78863331 0.78821042
0.78788961 0.7877946 0.78777726 0.78777511]
[0.75398268 0.77363428 0.78514119 0.78834856 0.78832451 0.78796063
0.78781342 0.78778035 0.78777546 0.78777495]
[0.77031116 0.78267477 0.78765759 0.78834516 0.78804071 0.78784268
0.78778631 0.78777625 0.78777503 0.78777492]
[0.78032012 0.78658571 0.78819847 0.78810517 0.78788161 0.7877965
0.78777791 0.78777521 0.78777493 0.78777491]
[0.78532201 0.78784377 0.7881183 0.78792393 0.78781177 0.78778099
0.78777561 0.78777497 0.78777492 0.78777491]
[0.7873102 0.78804598 0.78795672 0.78783132 0.78778607 0.78777643
0.78777506 0.78777492 0.78777491 0.78777491]]
```
## Build
Build docker image
```bash
docker build -t revotech-wi-contouring .
```


