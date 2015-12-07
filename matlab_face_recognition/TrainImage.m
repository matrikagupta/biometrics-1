clear
clc
trainSet = load_database(1);
N=20; 

%% Subtracting the mean from trainSet

tempmatrix=uint8(ones(1,size(trainSet,2)));    % empty matrix of 1*No of training set
trainSetMean=uint8(mean(trainSet,2));          % Mean of all training images
% save('MeanTrainSet.mat','trainSetMean');         % create database trainSetMean
csvwrite('feature_vectors/trainSetMean.csv',trainSetMean)
trainSetExMean=trainSet-uint8(single(trainSetMean)*single(tempmatrix));   % trainSetExMean is training set with the mean removed. 

%% Calculating eignevectors 
covariance=single(trainSetExMean)'*single(trainSetExMean); % Covariance C=A'A
[eigVector,D]=eig(covariance);
eigVector=single(trainSetExMean)*eigVector;     % multiple  for each image trainSetExMean set with eigen vector
eigVector=eigVector(:,end:-1:end-(N-1));        % Pick the eignevectors corresponding to the 20 largest eigenvalues. 
csvwrite('feature_vectors/eigVector.csv',eigVector)

%% Calculating the signature for each image
signaturevalue=zeros(size(trainSet,2),N);
for i=1:size(trainSet,2);
    signaturevalue(i,:)=single(trainSetExMean(:,i))'*eigVector;    % Each row in signaturevalue is the signature for one image.
end
csvwrite('feature_vectors/signaturevalue.csv',signaturevalue)
display('Training Completed!')

