function TestImage(InputImgPath)
Im=imread(InputImgPath);
% Imresize = imresize(Im,[112 92]);
TestImage=zeros(67600,1);
 TestImage(:,1)=reshape(Im,size(Im,1)*size(Im,2),1);
% TestImage(:,1)=Im;
% vt(:,0)=Imresize;
testFinalImg=uint8(TestImage);
%% Recognition 
subplot(121); 
imshow(reshape(testFinalImg,260,260));title('Looking for ...','FontWeight','bold','Fontsize',16,'color','blue');
trainSetMean=uint8(csvread('feature_vectors/trainSetMean.csv'));
signaturevalue=csvread('feature_vectors/signaturevalue.csv');
eigVector=csvread('feature_vectors/eigVector.csv');


subplot(122);
p=testFinalImg-trainSetMean; % Subtract the mean
s=single(p)'*eigVector;
z=[];
trainSet = load_database(0);
for i=1:size(trainSet,2)
    z=[z,norm(signaturevalue(i,:)-s,2)];
    if(rem(i,20)==0),imshow(reshape(trainSet(:,i),260,260)),end;
    drawnow;
end

[a,i]=min(z);
subplot(122);
imshow(reshape(trainSet(:,i),260,260));title('Found!','FontWeight','bold','Fontsize',16,'color','blue');


