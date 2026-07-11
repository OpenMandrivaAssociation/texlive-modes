%global tl_name modes
%global tl_revision 77365

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.4
Release:	%{tl_revision}.1
Summary:	A collection of Metafont mode_defs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/modes
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modes.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/modes.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The modes file collects all known Metafont modes for printing or display
devices, of whatever printing technology. Special provision is made for
write-white printers, and a 'landscape' mode is available, for making
suitable fonts for printers with pixels whose aspect is non-square. The
file also provides definitions that make \specials identifying the mode
in Metafont's GF output, and put coding information and other Xerox-
world information in the TFM file.

