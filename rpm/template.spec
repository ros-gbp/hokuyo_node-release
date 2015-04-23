Name:           ros-jade-hokuyo-node
Version:        1.7.8
Release:        0%{?dist}
Summary:        ROS hokuyo_node package

Group:          Development/Libraries
License:        LGPL
URL:            http://www.ros.org/wiki/hokuyo_node
Source0:        %{name}-%{version}.tar.gz

Requires:       log4cxx-devel
Requires:       ros-jade-diagnostic-updater
Requires:       ros-jade-driver-base
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-rosconsole
Requires:       ros-jade-roscpp
Requires:       ros-jade-self-test
Requires:       ros-jade-sensor-msgs
BuildRequires:  log4cxx-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-diagnostic-updater
BuildRequires:  ros-jade-driver-base
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-rosconsole
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-self-test
BuildRequires:  ros-jade-sensor-msgs

%description
A ROS node to provide access to SCIP 2.0-compliant Hokuyo laser range finders
(including 04LX).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Wed Apr 22 2015 Chad Rockey <chadrockey@gmail.com> - 1.7.8-0
- Autogenerated by Bloom

