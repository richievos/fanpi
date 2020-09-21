from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import url_for

from fanpi.fan import Fan

bp = Blueprint("blog", __name__)

fan = Fan.build_rpi([0, 1, 2])


def speed_class(speed, current_speed):
    if speed == current_speed:
        return 'current'
    else:
        return ''


def speed_states(speeds, current_speed):
    return [{'speed': speed,
             'class': speed_class(speed, current_speed)}
            for speed in speeds]


@bp.route("/", methods=["GET"])
# @login_required
def index():
    """View the current state of the fan"""
    states = speed_states(speeds=fan.get_speeds(),
                          current_speed=fan.get_current_speed())
    return render_template("fan.html", speeds=states)


@bp.route("/set_speed", methods=["POST"])
# @login_required
def set_speed():
    """Set the fan speed"""

    speed_arg = request.args.get('speed')
    if speed_arg is not None:
        speed = int(speed_arg)
        # @fan.set_speed(speed)
        print('yo')

    return redirect(url_for("fan.index"))
