# resume_writer.gemspec
#

Gem::Specification.new do |s|
  s.name          = "resume_writer".freeze
  s.version       = "0.0.1-alpha"
  s.authors       = ["Leam Hall"]
  s.email         = "freetradeleague@gmail.com"
  s.homepage      = "https://github.com/LeamHall/resume_writer"
  Dir.glob("bin/*").each {|f|
    s.executables   << File.basename(f)
  }
  s.licenses      = ["MIT"]
  s.platform      = Gem::Platform::RUBY
  s.summary       = "Produces resume in various formats."
  s.description   = "Using a single data set, produces resumes in short and long format, as well as text and html."
  s.files         = Dir.glob("{bin,data,docs,lib}/**/*")
  s.require_paths = ["lib"]
  s.datadir       << "data"
  s.add_development_dependency  'rspec', '~> 3'
  s.add_development_dependency  'rspec-mocks', '~> 3'
  s.add_development_dependency  'rspec-expectations', '~> 3'
end
