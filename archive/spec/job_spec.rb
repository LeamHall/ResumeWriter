# job_spec.rb
#

require 'resume_writer'
module ResumeWriter

  RSpec.describe 'a job' do
    data = Hash.new 
    let (:job) { ResumeWriter::Job.new(data) }

  it 'has a title' do
    expect(job.title.class).to eq(String)
  end

  end
end
