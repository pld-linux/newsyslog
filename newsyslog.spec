Summary:	Logfile Rotation Tool
Name:		newsyslog
Version:	1.1
Release:	0.1
License:	BSD
Group:		Base
URL:		http://www.weird.com/~woods/projects/newsyslog.html
Source0:	ftp://ftp.weird.com/pub/local/%{name}-%{version}.tar.gz
# Source0-md5:	022eb25d8ea236c07f6bcb0084b7e205
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Newsyslog is a program that is scheduled to run periodically by
cron(8) for archiving log files. If a log file is determined to
require archiving, newsyslog rearranges the files so that `logfile' is
empty, `logfile.0' has the last period's logs in it, `logfile.1' has
the next to last period's logs in it, and so on, up to a
user-specified number of archived logs. The archived logs may also be
compressed to save space. After all file operations are done newsyslog
notifies the syslogd daemon, or optionally some log-file specific
daemon, by sending a SIGHUP to the daemon process.

%prep
%setup -q

%build
%configure \
	--with-newsyslog_conf=%{_sysconfdir}/newsyslog/newsyslog.conf \
	--localstatedir=/var/lib/newsyslog \
	--with-syslog_pid=/var/run/newsyslog/newsyslog.pid \
	--with-gzip

%{__make} newsyslog copy-dist-mans

%install
rm -rf $RPM_BUILD_ROOT
# XXX patch Makefile.am
%{__make} install \
	htmlman_MANS= \
	catman_MANS= \
	catmandir=$RPM_BUILD_ROOT/tmp/cats \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING NEWS README ToDo VERSION newsyslog.conf
%attr(755,root,root) %{_bindir}/newsyslog
%{_mandir}/man5/newsyslog.conf.5*
%{_mandir}/man8/newsyslog.8*
