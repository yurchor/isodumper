Name:		isodumper
Version:	0.20
Release:	%mkrel 1
Summary:	Tool for writing ISO images on a USB stick
Summary(fr_FR):	Outil pour écrire des images ISO sur une clé USB
License:	GPLv2
Group:		System/Configuration
URL:		https://github.com/papoteur-mga/isodumper
# wget https://github.com/papoteur-mga/isodumper/archive/%%{version}.tar.gz -O %%{name}-%%{version}.tar.gz
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	imagemagick

Requires:	coreutils
Requires:	udisks
Requires:	procps
Requires:	python
Requires:	xterm
Requires:	pygtk2.0-libglade
Requires:	usermode-consoleonly

%description
A GUI tool for writing ISO images on a USB stick.
It's a fork of usb-imagewriter.

This software is written in python.

%description -l fr_FR
Un outil graphique pour écrire des images ISO sur une clé USB.
C'est un fork de usb-imagewriter

Ce logiciel est écrit en python.

#--------------------------------------------------------------------
%prep
%setup -q

%build
%make

%install
%makeinstall_std PREFIX="%{_prefix}"

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING CHANGELOG
%{_sbindir}/%{name}
%{_bindir}/%{name}
%{_usr}/lib/%{name}/
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

